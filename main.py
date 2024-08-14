import fileOrganizer as fo
import menu

downloads = fo.FileOrganizer(r"C:\Users\metin\Downloads")
downloads.partByExtension()
downloads.deleteAfterDeterminedTime()
#deneme = fo.FileOrganizer(r"C:\Users\metin\OneDrive\Masaüstü\kita\kita",dtime=7,doDel=0,doPart=0)
#fo.FileOrganizer.fOrgs.append(downloads)
m = menu.Menu(fo.FileOrganizer.fOrgs)
m.mainMenu()

fo.FileOrganizer.updateAllSaves()
