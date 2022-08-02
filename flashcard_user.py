import os
import json
import datetime
import sys
# Define function to import external files when using PyInstaller.
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
class User:
    
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.totalTime = '00:00:00'
        
    def login(self):
        userFile = resource_path('users')
        if not os.path.exists("{}/{}.json".format(userFile,self.name)):
            myDict={
                "name":self.name,
                "level":self.level,
                "totalTime":self.totalTime,
            }
            with open("{}/{}.json".format(userFile,self.name),"w") as json_file:
                json.dump(myDict,json_file,indent=4)
                
        with open("{}/{}.json".format(userFile,self.name),"r") as json_file:
            data = json.load(json_file)
            self.level = data["level"]
            self.totalTime = data["totalTime"]
            
    def registerUserStat(self,lastlevel,passedtime):
        userFile = resource_path('users')
        my_file = open("{}/{}.json".format(userFile,self.name),"r")
        data = json.load(my_file)
        my_file.close()
        data["level"] = lastlevel
        self.level = lastlevel
        h,m,s = data["totalTime"].split(":")
        totalseconds = int(h)*3600+int(m)*60+int(s) + int(passedtime)
        self.converted_time = str(datetime.timedelta(seconds=totalseconds))
        data["totalTime"] = self.converted_time
        self.totalTime = self.converted_time
        my_file = open("{}/{}.json".format(userFile,self.name),"w")
        json.dump(data,my_file,indent = 4)
        my_file.close()