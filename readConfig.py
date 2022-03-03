import os
import codecs
import configparser

proDir=os.path.split(os.path.realpath(__file__))[0]
configPath=os.path.join(proDir,"pytest.ini")

class ReadConfig():
    def __init__(self):
        with open(configPath) as file:
            data=file.read()
            if data[:3]==codecs.BOM_UTF8:
                data=data[3:]
                file=codecs.open(configPath,"w")
                file.write(data)
            self.cf=configparser.RawConfigParser()
            self.cf.read(configPath)
    def get_http(self,name):
        value=self.cf.get("HTTP",name)
        return value
    def get_variable(self,name):
        value=self.cf.get("variable",name)
        return value



