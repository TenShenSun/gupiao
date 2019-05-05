# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import threading
import tkinter as tk  # 使用Tkinter前需要先导入

from scrapy.cmdline import execute
import sys,os

import tkinter.messagebox
import pickle

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('股票预测系统')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x400')  # 这里的乘是小x

# 第4步，加载 wellcome image
canvas = tk.Canvas(window, width=400, height=135, bg='green')
image_file = tk.PhotoImage(file='stock.gif')
image = canvas.create_image(200, 20, anchor='n', image=image_file)
canvas.pack(side='top')
tk.Label(window, text='Wellcome', font=('Arial', 16)).pack()

def crawl_thread():
    # 获得当前文件的绝对路径
    # print(os.path.abspath(__file__))
    # 获得当前路径的父目录
    # sys.path当前系统的环境变量
    # 把路径放入系统的环境变量中
    # print(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # execute(['scrapy', 'crawl', 'gupiao2','-a','start_date=20180417','end_date=20190412','code=000725'])

    # 判断股票代码是否为空
    if stockCode.get()!='':
        code = stockCode.get()
    else:
        tkinter.messagebox.showinfo('提示', 'stockCode must set！！！')

    # 判断开始日期是否为空
    if startDate.get()!='':
        start_date = startDate.get()
    else:
        tkinter.messagebox.showinfo('提示', 'startDate must set！！！')

    # 判断结束日期是否为空
    if endDate.get()!='':
        end_date = endDate.get()
    else:
        tkinter.messagebox.showinfo('提示', 'endDate must set！！！')


    if(stockCode.get()!='' and startDate.get()!='' and endDate.get()!=''):
        subprocess.Popen("scrapy crawl gupiao2 -a start_date=%s -a end_date=%s -a code=%s" %(start_date,end_date,code))

def crawl_fun():
    try:
        t = threading.Thread(target=crawl_thread)
        t.start()
        # 主线程要等到调用线程执行完毕后才能继续执行，会一直阻塞
        # t.join()
    except:
        print("Error: unable to start thread")


def predict_thread():
    # 获得当前文件的绝对路径
    # print(os.path.abspath(__file__))
    # 获得当前路径的父目录
    # sys.path当前系统的环境变量
    # 把路径放入系统的环境变量中
    # print(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # execute不能用在python命令上
    # execute(['python', 'D:\gupiao\gupiaospider\predict2'])
    # subprocess可以用
    subprocess.Popen("python predict2.py %s" %stockCode.get(),shell=True)

def predict_fun():
    try:
        t = threading.Thread(target=predict_thread)
        t.start()
        # 主线程要等到调用线程执行完毕后才能继续执行，会一直阻塞
        # t.join()
    except:
        print("Error: unable to start thread")



# 第5步，爬虫 预测 按钮

stockLabel=tkinter.Label(text="StockCode：") #标签
stockLabel.place(x=100,y=200)
stockCode=tkinter.Entry() #创建文本框
#stockCode=tkinter.Text(window,width = 8,height = 1)
stockCode.place(x=200,y=200)

startDateLabel=tkinter.Label(text="start_date：") #标签
startDateLabel.place(x=100,y=230)
startDate=tkinter.Entry() #创建文本框
startDate.place(x=200,y=230)

endDateLabel=tkinter.Label(text="endDate：") #标签
endDateLabel.place(x=100,y=260)
endDate=tkinter.Entry() #创建文本框
endDate.place(x=200,y=260)


btn_crawl = tk.Button(window, text='crawl',width=15,height=2, command=crawl_fun)
btn_crawl.place(x=100, y=290)
btn_predict = tk.Button(window, text='predict',width=15,height=2, command=predict_fun)
btn_predict.place(x=240, y=290)

# 第6步，主窗口循环显示
window.mainloop()