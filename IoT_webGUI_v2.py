from urllib.request import urlopen
from tkinter import *
import json
import time
import numpy as np
from sklearn.metrics.pairwise import manhattan_distances
from sklearn.neighbors import KDTree
from sklearn import tree
from sklearn.neighbors.classification import KNeighborsClassifier
from timeit import default_timer as timer
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import KFold



win=Tk()
win.title("I want to skip the class")
width = 600
height = 250
screenwidth = win.winfo_screenwidth()
screenheight = win.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
win.geometry(alignstr)    # 居中对齐

win = Frame()
win.pack(expand=YES)

label=Label(win, height=1, text="Please enter the location name :")#建立標籤物件
label.grid(row=1, pady=10)
label2=Label(win, height=1, text="Yes for attend and no for skip :    ")#建立標籤物件
label2.grid(row=10)

e=Entry(win, justify=CENTER ,width=14)
e.grid(row=1, column=1)

#e2=Entry(win, justify=CENTER ,width=14)
#e2.grid(row=10, column=1)

var7 = StringVar()    # 这时文字变量储存器

e2=Radiobutton(win, text='Yes', variable=var7, value='yes')
e2.grid(row=10, column=1, stick=W)
e3=Radiobutton(win, text='No', variable=var7, value='no')
e3.grid(row=10, column=1, columnspan=2)

def hit_me():
    str="http://api.wunderground.com/api/f4d4d2cde7f948ec/geolookup/conditions/q/TW/"+e.get()+".json"
    str2="http://api.wunderground.com/api/f4d4d2cde7f948ec/hourly/q/TW/"+e.get()+".json"
    f1 = urlopen(str)
    json_string1 = f1.read().decode('utf-8')
    parsed_json1 = json.loads(json_string1)
    location_TP = parsed_json1['location']['city']
    temp_TP = parsed_json1['current_observation']['temp_c']
    rain_TP = parsed_json1['current_observation']['precip_today_metric']

    f2 = urlopen(str2)
    json_string2 = f2.read().decode('utf-8')
    parsed_json2 = json.loads(json_string2)
    temp_HR = parsed_json2['hourly_forecast'][1]['temp']['metric']
    rain_HR = parsed_json2['hourly_forecast'][1]['pop']


    
    temp_TP=float(temp_TP)
    if rain_TP.isdigit():
        rain_TP=float(rain_TP)
    else:
        rain_TP=0
    temp_HR = float(temp_HR)
    rain_HR = float(rain_HR)
    ticks = time.asctime( time.localtime(time.time()) )

    if rain_TP<0:
        rain_TP=0
    if rain_TP<0:
        rain_TP=0

    var1.set("Current temperature in %s is: %d celsius" % (location_TP, temp_TP))
    var2.set("Rainfall of past hour in %s is: %d" % (location_TP, rain_TP))
    var4.set("Next hour temperature in %s is: %d celsius" % (location_TP, temp_HR))
    var5.set("Next hour Precipitation in %s is: %d" % (location_TP, rain_HR))
    var6.set(ticks)

    nowdata=np.zeros(4)
    nowdata[0]=temp_TP
    nowdata[1]=rain_TP
    nowdata[2]=temp_HR
    nowdata[3]=rain_HR

    data = np.genfromtxt('data.txt', delimiter=" ")
    target = np.genfromtxt('data.txt', delimiter=" ",usecols=(4))
    attribute = data[:,0:4]
    print(attribute)

    dtc= tree.DecisionTreeClassifier(max_depth=10)
    r=dtc.fit(attribute, target)
    pred = dtc.predict(nowdata)
    print(pred)



    if (pred==2):
        var3.set("I suggest that you should skip the class")

    else:
        var3.set("I suggest that you should attend the class")


    f1.close()
    f2.close()

def hit_ok():
    
    str1="http://api.wunderground.com/api/f4d4d2cde7f948ec/geolookup/conditions/q/TW/"+e.get()+".json"
    str2="http://api.wunderground.com/api/f4d4d2cde7f948ec/hourly/q/TW/"+e.get()+".json"
    f1 = urlopen(str1)
    json_string1 = f1.read().decode('utf-8')
    parsed_json1 = json.loads(json_string1)
    location_TP = parsed_json1['location']['city']
    temp_TP = parsed_json1['current_observation']['temp_c']
    rain_TP = parsed_json1['current_observation']['precip_today_metric']
    
    f2 = urlopen(str2)
    json_string2 = f2.read().decode('utf-8')
    parsed_json2 = json.loads(json_string2)
    temp_HR = parsed_json2['hourly_forecast'][1]['temp']['metric']
    rain_HR = parsed_json2['hourly_forecast'][1]['pop']
    
    
    
    temp_TP=float(temp_TP)
    if rain_TP.isdigit():
        rain_TP=float(rain_TP)
    else:
        rain_TP=0
    temp_HR = float(temp_HR)
    rain_HR = float(rain_HR)
    ticks = time.asctime( time.localtime(time.time()) )

    if rain_TP<0:
        rain_TP=0
    if rain_TP<0:
        rain_TP=0

    var8 = var7.get()
    if var8=='yes':
        f = open('data.txt','a')
        nwstring = '\n'+str(temp_TP)+' '+str(rain_TP)+' '+str(temp_HR)+' '+str(rain_HR)+' 1'
        f.write(nwstring)
    if var8=='no':
        f = open('data.txt','a')
        nwstring = '\n'+str(temp_TP)+' '+str(rain_TP)+' '+str(temp_HR)+' '+str(rain_HR)+' 2'
        f.write(nwstring)



b = Button(win,
    text='OK',      # 显示在按钮上的文字
    command=hit_me, width=5)   # 点击按钮式执行的命令  
b.grid(row=1, column=2, stick=E)


b = Button(win,
           text='OK',      # 显示在按钮上的文字
           command=hit_ok, width=5)   # 点击按钮式执行的命令
b.grid(row=10, column=2, stick=W)





var1 = StringVar()    # 这时文字变量储存器
var2 = StringVar()    # 这时文字变量储存器
var3 = StringVar()    # 这时文字变量储存器
var4 = StringVar()    # 这时文字变量储存器
var5 = StringVar()    # 这时文字变量储存器
var6 = StringVar()    # 这时文字变量储存器

l1 = Label(win,
    textvariable=var1   # 使用 textvariable 替换 text, 因为这个可以变化
    )
l1.grid(row=3, columnspan=2)
l2 = Label(win,
    textvariable=var2   # 使用 textvariable 替换 text, 因为这个可以变化
    )
l2.grid(row=4, columnspan=2)
l4 = Label(win,
    textvariable=var4   # 使用 textvariable 替换 text, 因为这个可以变化
    )
l4.grid(row=5, columnspan=2)
l5 = Label(win,
    textvariable=var5   # 使用 textvariable 替换 text, 因为这个可以变化
    )
l5.grid(row=6, columnspan=2)


temp = Label(win,
    text=""   
    )
temp.grid(row=7, columnspan=2)


l3 = Label(win,
    textvariable=var3,   # 使用 textvariable 替换 text, 因为这个可以变化
    fg="red",			 # 字體顏色
    font=('times', 16, 'bold') # 字型, 大小
    )
l3.grid(row=8, columnspan=2)

l6 = Label(win,
           textvariable=var6   # 使用 textvariable 替换 text, 因为这个可以变化
           )
l6.grid(row=9, columnspan=2)


win.mainloop()

