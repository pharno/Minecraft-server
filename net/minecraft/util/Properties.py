from net.minecraft.util.logger import logger

class Properties:
    def __init__(self):
        self.properties = {}

    def load(self,fil):
        lines = fil.readlines()

        for line in lines:
            if line[0] in ["#","!","\n"]:
                continue
            
            key,value = line[:-1].split("=")
            self.properties[key] = value

    def store(self,fil,comments):
        out = "\n".join(comments)
        print out
    
    def containsKey(self,key):
        if key in self.properties.keys():
            return True
        else:
            return False

    def setProperty(self,key,value):
        self.properties[key] = value

    def getProperty(self,key):
        return self.properties[key]