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
                print(files)
            print("********************************************")
            print("Options:")
            print("1) Add Folder    2)Edit Folder")
            print("3) Exit")

            self.menuSelection = input()
            while(self.__inputControl(self.menuSelection)):
                pass
            #print(type(self.menuSelection))
            if self.menuSelection == 1:
                self.AddFolder()
            if self.menuSelection == 2:
                pass
            if self.menuSelection == 3:
                break #break olacak bu da şu an döngü yok diye
            
    def AddFolder(self):
        print("Please enter the path of the folder that you want to include the system")
        print(r"For example: C:\Users\metin\Downloads")
        path = input()
        folder = fo.FileOrganizer(path)


    def folderMenu(self):
        #mainmenude seçilen folderın bilgilerini değiştirme, görme falan yeri, sistemden kaldırma ayarı falan
        pass
    def __inputControl(self,menuSelection):
        try:
            self.menuSelection = int(menuSelection)
            if (self.menuSelection < 4 and self.menuSelection > 0):
                return False
            else:
                print("Please enter a valid number")
                self.__inputControl(input())
        except:
            print("Please enter a valid number")
            self.__inputControl(input())
