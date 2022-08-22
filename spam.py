from tkinter import *
import pyautogui
import os
import sys
import time

root = Tk()
root.configure(background="#2a2b31")

# Global var

spam = ""
user = ""
times = ""
with open("data/path.txt") as file:
    path = file.readline()
    pathh = path.rstrip("\n")
    num = file.readline()
    numm = int(num)
# Window specs

root.geometry("600x400")
root.title("Whatswapp Spamer by (Vihaan bhardwaj) ")
root.minsize(600,400)
root.maxsize(600,400)

# Funtiona

def cancel():
    print("exit")
    sys.exit()

def ok():
    spam = spam_entry.get()
    user = name_entry.get()
    try:
        times = int(entry.get())
    except:
        pyautogui.alert("put spam input in number")
    print(user)
    print(times)
    print(spam)
    os.startfile(pathh)
    time.sleep(numm)
    pyautogui.click(127,127)
    pyautogui.typewrite(user)
    pyautogui.click(134,305)
    pyautogui.click(880 , 966)
    for i in range(1,times+1):
        pyautogui.typewrite(spam)
        pyautogui.hotkey("enter")

# Labelss And Inputs

spam_input = Label(text="What do you what to spam: ",font=("Helvetica",10,"bold"),background="#2a2b31",foreground="#00ff00")
spam_input.grid(row = 4)
spam_entry = Entry(root,width= 40,)
spam_entry.grid(row = 4, column = 10,pady=20)
spam_entry.config(highlightbackground="red",highlightcolor="green",highlightthickness=4)

content = Label(text="Fill All The Entry down",font=("Helvetica",15,"bold"),background="#2a2b31",foreground="#6afbfb",relief="solid")
content.grid(row=0,column=10)

name_input = Label(text="Whatsapp name of that user: ",font=("Helvetica",10,"bold"),background="#2a2b31",foreground="#00ff00")
name_input.grid(row=6)
name_entry = Entry(root,width= 40)
name_entry.grid(row = 6, column = 10,pady=20)
name_entry.config(highlightbackground="red",highlightcolor="green",highlightthickness=4)

name_input = Label(text="times you want to spam: ",font=("Helvetica",10,"bold"),background="#2a2b31",foreground="#00ff00")
name_input.grid(row=8)
entry = Entry(root,width= 40)
entry.config(highlightbackground="red",highlightcolor="green",highlightthickness=4)
entry.grid(row = 8, column = 10,pady=20)

# BUtton

b1 = Button(root,text="OK",width=20,background="pink",command=ok)
b1.grid(row=20,column=10)
b2 = Button(root,text="CANCEL",background="pink",width=20,command=cancel)
b2.grid(row=30,column=10,pady=25)

# Mainloop

root.mainloop()

