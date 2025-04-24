# Importing Tkinter()
from tkinter import * # type: ignore

# Root window
root = Tk() # creating main window but it will be closed within few seconds
# all the code will be written in between the Tk() object and mainloop(infinite loop)

# making fixed window size
root.geometry('300x400')

# creating hello world widget
hello = Label(root, text='Hello world')

# inputing hello widget into the root window
hello.pack()

root.mainloop() # this is going to keep the window open until we close them.