from tkinter import *
from tkinter import messagebox

def getInput():
    input = inputTxt.get(1.0, "end-1c")
    pass
def fillFilesListBox():
    fileListBox.insert(1,"deneme")
    fileListBox.insert(2,"deneme2")
    pass
def call_edit_page(fileName,fileIndex):
    ep_file_name_txt = Label(edit_page,text="Editing File: \n"+fileName).grid(column=0,row=0,sticky="wesn",columnspan=5)
    current_delTime = Label(edit_page,text="Current delTime: \n").grid(column=0,row=1,sticky="wesn",pady=5)
    current_doDel = Label(edit_page,text="Current doDel: \n").grid(column=0,row=2,sticky="wesn",pady=5)
    current_doPart = Label(edit_page,text="Current doPart: \n").grid(column=0,row=3,sticky="wesn",pady=5)
    #buttons
    change_deltime_button = Button(edit_page,text="change delTime").grid(column=4,row=1,sticky="wesn",pady=5)
    change_dodel_button = Button(edit_page,text="change doDel").grid(column=4,row=2,sticky="wesn",pady=5)
    change_dopart_button = Button(edit_page,text="change doPart").grid(column=4,row=3,sticky="wesn",pady=5)
    exclude_from_system_button = Button(edit_page,text="excluede from\nsystem").grid(column=4,row=4,sticky="wesn",pady=30)
    exit_edit_page_button = Button(edit_page,text="return to \n main page",command=exit_edit_page).grid(column=0,row=5,sticky="wesn")



    edit_page.tkraise()

    pass

def exit_edit_page():
    main_page.tkraise()
    pass

def editSelectedFile():
    selection = fileListBox.curselection()
    if selection:
        #messagebox.showinfo("aa","aa")
        
        call_edit_page(fileListBox.get(selection),selection)
        pass
    pass

listbox_w = 50
textbox_W = 40
main =Tk()
main.title("File Organizer")
main.geometry("500x400")

main_page = Frame(main)
edit_page = Frame(main)

main.columnconfigure((0,0),weight=1,uniform="a")
main.rowconfigure((0,0),weight=1,uniform="a")

edit_page.grid(row=0,column=0,sticky="wesn")
main_page.grid(row=0,column=0,sticky="wesn")
#widgets are added here... 

fileListBox = Listbox(main_page)
inputTxt = Text(main_page,height=1)
inputTxtButton = Button(main_page,text="Add File",command=getInput)
editFileButton = Button(main_page,text="Edit File", command=editSelectedFile)

#grids
main_page.columnconfigure((0,1),weight=1,uniform="a")
main_page.rowconfigure((0,5),weight=1,uniform="a")

edit_page.columnconfigure((0,1),weight=1,uniform="a")
edit_page.rowconfigure((0,5),weight=1,uniform="a")

fileListBox.grid(row=0,column=0,sticky="ew",pady=2, columnspan=3)
editFileButton.grid(row=0,column=5,sticky="ew",pady=2)
inputTxt.grid(row=2,column=0,sticky=W,pady=2, columnspan=3)
inputTxtButton.grid(row=2,column=5,sticky=W,pady=2)

#functions,rendering etc.
fillFilesListBox()

main_page.tkraise()
main.mainloop()