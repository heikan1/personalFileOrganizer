import os
import time
import datetime
import shutil

class FileOrganizer:
    fOrgs = []
    def __init__(self,path,dtime = None):
        self.files = os.listdir(path)
        self.deleteTime = dtime
        self.path = path
        FileOrganizer.fOrgs.append(path)
        self.saveToTxt()

    ##şunda readline bozuk ya anlamadım, gelince halledersin
    def saveToTxt(self):
        print("0")
        txt = open("folders.txt","r+") #modla alakalı
        lines = txt.readlines()
        doesExist = False
        #print(lines)
        for file in FileOrganizer.fOrgs:
            print("1")
            #print(lines)
            for line in lines:
                print("2")
                line = line.replace("\n","")
                #print(line + " " + file)
                if line == file:
                    print("3")
                    doesExist = True
            if not doesExist:
                txt.write(file + "\n")
        txt.close
        pass
    def removeFromTxt(self):
        pass
    def __del__(self):
        pass
    def partByExtension(self):
        for file in self.files:
            fileName, fileExtension = os.path.splitext(file)
            fileExtension = fileExtension[1:]

            if not os.path.exists(self.path + "/" + fileExtension):
                os.makedirs(self.path+"/"+fileExtension)
            shutil.move(self.path + "/" + file, self.path + "/" + fileExtension + "/" + file)
            
    def deleteAfterDeterminedTime(self):
        if self.deleteTime == None:
            return
        now = datetime.datetime.now()
        for file in self.files:
            ti_c = os.path.getctime(self.path)
            ti_c = datetime.datetime.fromtimestamp(ti_c)
            if int((now - ti_c).days) > self.deleteTime:
                os.remove(self.path+"/"+file)
        