import fileOrganizer as fo
class Menu(object):
    #singleton model
    def __new__(cls, fileOrgList):
        if not hasattr(cls,'instance'):
            cls.instance = super(Menu,cls).__new__(cls)
        return cls.instance
    
    def __init__(self,fileOrgList):
        self.menuSelection = None
        pass      
    def mainMenu(self):
        #sisteme eklenmiş tüm folderları gösteren, yeni folder ekleme işlemlerinin falan olduğu yer olacak
        while True:
            print("********************************************")
            for files in fo.FileOrganizer.fOrgs:
                print(files.path)
            print("********************************************")
            print("Options:")
            print("1) Add Folder    2)Edit Folder")
            print("3) Exit")

            self.menuSelection = input()
            while(self.__inputControl(self.menuSelection,4,0)):
                pass
            #print(type(self.menuSelection))
            if self.menuSelection == 1:
                self.AddFolder()
            if self.menuSelection == 2:
                self.folderMenu()
            if self.menuSelection == 3:
                break #break olacak bu da şu an döngü yok diye
            
    def AddFolder(self):
        print("Please enter the path of the folder that you want to include the system")
        print(r"For example: C:\Users\metin\Downloads")
        path = input()
        folder = fo.FileOrganizer(path)
        print("Folder has successfully added!")


    def folderMenu(self):
        #mainmenude seçilen folderın bilgilerini değiştirme, görme falan yeri, sistemden kaldırma ayarı falan
        print("Please enter the index of a folder that you want to edit:")
        print(f"Between {0} and {fo.FileOrganizer.fOrgs.__len__()-1}")
        fIndex = self.__inputControl(input(),fo.FileOrganizer.fOrgs.__len__(),-1)

        print("********************************************")
        print("Folder:")
        print(fo.FileOrganizer.fOrgs[fIndex].path)
        print("Options:")
        print("1) Delete from system")
        print("2) Change delTime")
        print("3) Change doDel")
        print("4) Change doPart")
        print("0) Turn back to main menu")
        print("********************************************")
        selection = self.__inputControl(input("Index of option: "),5,-1)

        #dont forget that i have fIndex by now
        #so i can just type all functions in this class???
        #maybe i should not lol.
        #uh even though i wont i need to pass the fIndex to the functions
        match selection:
            case 0:
                self.mainMenu()
            case 1:
                fo.FileOrganizer.deleteFolderfromSystem(fIndex)
                print("Successfully deleted")
                #will add delete function later
                pass
            case 2:
                print(f"Current dtime is {fo.FileOrganizer.fOrgs[fIndex].deleteTime} days.")
                new_d = self.__inputControl(input("What do you want to change with: "),100000,-1)
                fo.FileOrganizer.updateFolderSettings(fIndex,dTime=new_d)
                print("Chage has successfully made")
                pass
            case 3:
                print(f"Current doDel is {fo.FileOrganizer.fOrgs[fIndex].doDel} .")
                new_d = self.__inputControl(input("What do you want to change with (1 is True, 0 is False): "),2,-1)
                if(new_d == 1):
                    new_d = True
                else:
                    new_d = False
                fo.FileOrganizer.updateFolderSettings(fIndex,doDel=new_d)
                print("Chage has successfully made")
                pass
            case 4:
                print(f"Current doPart is {fo.FileOrganizer.fOrgs[fIndex].doPart} .")
                new_d = self.__inputControl(input("What do you want to change with (1 is True, 0 is False): "),2,-1)
                if(new_d == 1):
                    new_d = True
                else:
                    new_d = False
                fo.FileOrganizer.updateFolderSettings(fIndex,doPart=new_d)
                print("Chage has successfully made")
                pass
            case _:
                self.mainMenu()
                pass
        self.mainMenu()
        pass
    def __inputControl(self,menuSelection,upperlimit,lowerlimit):
        try:
            self.menuSelection = int(menuSelection)
            if (self.menuSelection < upperlimit and self.menuSelection > lowerlimit):
                return False
            else:
                print("Please enter a valid number")
                self.__inputControl(input(),upperlimit,lowerlimit)
        except:
            print("Please enter a valid number")
            self.__inputControl(input(),upperlimit,lowerlimit)
