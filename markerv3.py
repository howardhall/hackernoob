#!/usr/bin/python3
import os, subprocess, sys, time, json, sqlite3, markers, traceback, hashlib
class Marker:
    def __init__(self):
        self.setup_db()

    def setup_db(self):
        self.conn = sqlite3.connect("db.sqlite3")
        self.db = self.conn.cursor()

    def commit_db(self):
        self.conn.commit()

    def execute(self):
        # execute subclass of programming language
        # should be an interface lol
        pass

    def setup(self,id):
        query = "SELECT * FROM tests WHERE id = {}".format(id[0])
        result = self.db.execute(query)
        for i in result:
            self.id = i[0]
            self.format = i[1]
            self.time = i[4] - i[3]
            self.type = i[2]
            self.name = i[7]
            return

    def store(self):
        query = "UPDATE tests SET result = {}, marked = 1 WHERE id = {}".format(self.score,self.id)
        self.db.execute(query)
        return self.db.rowcount

    def load(self):
        query = "SELECT details, timer FROM exams WHERE id = {}".format(self.type)
        for i in self.db.execute(query):
            self.json_name = i[0]
            self.time = i[1]
            break
        datafile = open("solutions/{}.json".format(self.json_name))
        self.result = json.loads(datafile.read())
        #print(self.result)

    def prepare(self):
        #name = hashlib.md5(str(self.id).encode()).hexdigest()
        name = self.name
        if self.format == "py":
            self.markable = markers.PyMark(name)# TODO change to value in db
        # other cases

    def examine(self):
        self.score = 0
        for test in self.result['tests']:
            guess = self.markable.execute(test['param'])
            if guess == test['answer']:
                self.score += test['mark']

    def check_new(self):
        query = "SELECT * FROM tests WHERE marked=0;"
        results = []
        for id in self.db.execute(query):
            results.append(id)
        return results

    def error(self):
        query = "UPDATE tests SET result = 0, marked = 1 WHERE id = {}".format(self.id)
        self.db.execute(query)
        return self.db.rowcount

    def main(self):
        while True:
            pending = self.check_new()
            if len(pending) == 0:
                for i in range(60):
                    print("Waiting {} seconds before next check".format(60-i),end="\r")
                    time.sleep(1)
                continue

            try:
                self.setup(pending[0])
                self.load()
                self.prepare()
                self.examine()
                self.store()
                print("Sucessfully marked test id {}, mark = {}".format(self.id,self.score))
            except FloatingPointError:
                print("marking test with id {} failed".format(pending[0][0]))
                self.error()
            except Exception:
                print("MAJOR SYSTEM ERROR, BIG F")
                traceback.print_exc(file=sys.stdout)
                sys.exit(13)
            self.commit_db()

if __name__ == '__main__':
    mark = Marker()
    #sys.exit()
    mark.main()
