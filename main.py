import fileOrganizer as fo
import menu

downloads = fo.FileOrganizer(r"C:\Users\metin\Downloads",7)
downloads.partByExtension()
downloads.deleteAfterDeterminedTime()
fo.FileOrganizer.fOrgs.append(downloads)
m = menu.Menu(fo.FileOrganizer.fOrgs)
m.mainMenu()