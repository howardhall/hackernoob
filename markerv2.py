#!/usr/bin/python3
import os, subprocess, sys, time, json, sqlite3
def execute_py(params):
    sys.path.append("working")
    from marking import answer
    return answer(*params)

def execute_java(params):
    pass
def execute_c(params):
    pass
def execute_cpp(chparams):
    pass
def execure_php(params):
    pass

def execute(params, format):
    if format == "py":
        return execute_py(params)

def setup(name,format):
    if format == "py":
        subprocess.run("cp {}.txt working/marking.py".format(name));

def cleanup(format):
    if format == "py":
        subprocess.run("rm working/marking.py");

def examine(tests, format):
    score = 0
    for test in tests:
        if(execute(test.params,format) == test.answer):
            score += test.mark
    return score

def store():
    pass
def test(data,filename):
    pass
# loads the file and returns a file object
def load_file(filename):
    pass

# compares the  user result to the system result and gives a mark
def mark(id,file,format):
    setup(file,format)
    jason = load_exam(id)
    mark = examine(jason,format)
    store(id,mark)
    cleanup(format)

# Returns an array containing all the ID's of the unmarked exams.
def check_new(db):
    query = "SELECT * FROM tests WHERE marked=0;"
    results = []
    for id in db.execute(query):
        results.append(id)
    return results

# main loop, will be set as system service.
def main():
    conn = sqlite3.connect("db.sqlite3")
    db = conn.cursor()
    while True:
        remaining = check_new(db)
        print(remaining)
        if len(remaining) != 0:
            print("unmarked {}".format(len(remaining)))
            mark("marking","py")
            time.sleep(3)
        else :
            print("all marked")
            time.sleep(3)
        #id = result[0]

if __name__ == '__main__':
    main()
    #print(execute(["howard",20],"py"))
