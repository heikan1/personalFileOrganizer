from tkinter import *

def testButtonFunc():
    testLabel3.config(text="Congratz!")
def getInput():
    input = testTxt.get(1.0, "end-1c")
    testTxtLabel.config(text = "Your input: "+input)
    pass

main =Tk()
main.title("File Organizer")
#widgets are added here... 
testLabel = Label(main,text="Hi!")
testLabel2 = Label(main,text="Hakan.")
testLabel3 = Label(main,text="")
testButton = Button(main, text="Click it!",command=testButtonFunc)
testTxt = Text(main,height=5,width=10)
testTxtButton = Button(main,text="Enter",command=getInput)
testTxtLabel = Label(main,text="Your input: ")

testLabel.pack()
testLabel2.pack()
testButton.pack()
testLabel3.pack()
testTxt.pack()
testTxtButton.pack()
testTxtLabel.pack()

main.mainloop()