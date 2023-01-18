from pytube import YouTube
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image



win = Tk()
win.title("Youtube downloader")
win.config(bg="green")
win.geometry("800x600") # width x height

my_img = ImageTk.PhotoImage(Image.open("./download.png"))
name = Label(win,text=" YOUTUBE VIDEO DOWNLOADER ",font=("Time New Roman",30,"bold"))
name.place(x=25, y=50,height=50,width=750)

entry = Entry(win,font=("Times New Roman", 15, "bold"))
entry.place(x=25,y=140,height=50,width=600)

win.mainloop()