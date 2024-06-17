import os
import time
import datetime
import shutil

class FileOrganizer:
    fOrgs = []
    def __init__(self,path,doDel = 0,doPart = 0,dtime = None):
        print(str(doDel)+ " " +str( doPart))
        self.files = os.listdir(path)
        self.deleteTime = dtime
        self.path = path
        self.doDel = doDel
        self.doPart = doPart
        FileOrganizer.fOrgs.append(self)
        self.index = FileOrganizer.fOrgs.__len__()
        self.firstSaveToTxt()
        #self.saveToTxt()

    ##şunda readline bozuk ya anlamadım, gelince halledersin
    def firstSaveToTxt(self):
        #print("0")
        txt = open("folders.txt","a") #modla alakalı
        #print(self.path)
        txt.write(self.path + "\n")
        txt.close

        txt = open("folderspecs.txt","a") #modla alakalı
        txt.write(str(self.doDel)+str(self.doPart)+str(self.deleteTime)+"\n")
        txt.close

    def updateAllSaves():
        print("a")
        txt = open("folders.txt","w")
        content = ""
        for folder in FileOrganizer.fOrgs:
            content += folder.path +"\n"
        txt.write(content)
        print(content)
        txt.close

        txt = txt = open("folderspecs.txt","w")
        content = ""
        for folder in FileOrganizer.fOrgs:
            content += str(folder.doDel)+str(folder.doPart)+str(folder.deleteTime)+"\n"
        txt.write(content)
        print(content)
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
            if os.path.isdir(self.path+"\\"+file):
                continue
            ti_c = os.path.getctime(self.path)
            ti_c = datetime.datetime.fromtimestamp(ti_c)
            if int((now - ti_c).days) > self.deleteTime:
                os.remove(self.path+"\\"+file)
        