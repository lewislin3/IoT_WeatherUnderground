from urllib.request import urlopen
import tkinter as tk
import json
import time



win=tk.Tk()
win.title("I want to skip the class")

label=tk.Label(win, text="Please key in the reigon")#建立標籤物件
label.pack()#顯示元件

e=tk.Entry(win)
e.pack()

def insert_point():
    var=e.get()
b1=tk.Button(win,text='OK',command=insert_point)
b1.pack()

t = tk.Text(win,height=2)
t.pack()




win.mainloop()

