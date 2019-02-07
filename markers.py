import subprocess, sys
class PyMark:
    def __init__(self,name):
        self.setup(name)

    def execute(self, params):
        ans = ""
        try:
            ans = self.ans(*params)
        except:
            raise FloatingPointError("marking threw an error")
        return ans

    def setup(self, name):
        #self.name = name
        data = ''
        try:
            data = open('submissions/{}.txt'.format(name),'r')
        except:
            raise FloatingPointError("file {} not found".format(name))
        next = open('marking.py','w')
        next.write(data.read())
        data.close()
        next.close()
        #subprocess.run("touch marking.py")
        #subprocess.run("cp submissions/{}.txt marking.py".format(name))
        #sys.path.append("working")
        #from marking import answer as answer
        try:
            self.ans = __import__('marking').answer
        except:
            raise FloatingPointError("answer wasn't even defined by the noob")

    def cleanup(self):
        subprocess.run("rm working/marking.py");

#class JavaMark:
#class CMark:
#class CppMark:
#class PHPMark:
