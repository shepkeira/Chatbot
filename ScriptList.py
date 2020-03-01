import Script
class ScriptList:
    def __init__(self, file):
        self.importScripts(file)
    def importScripts(self, file):
        try:
            scripts = []
            f=open(file, "r")
            f1 = f.readlines()
            for x in f1:
                script = Script.Script(x)
                scripts.append(script)
        except FileNotFoundError:
            print("File not found")

