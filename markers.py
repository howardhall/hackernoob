class PyMark:
    def __init__(self,name):
        self.setup(name)

    def execute(self, params):
        return answer(*params)

    def setup(self, name):
        subprocess.run("cp {}.txt working/marking.py".format(name))
        sys.path.append("working")
        from marking import answer

    def cleanup(self):
        subprocess.run("rm working/marking.py");

#class JavaMark:
#class CMark:
#class CppMark:
#class PHPMark:
