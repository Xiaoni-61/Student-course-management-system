#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/10/8 21:42
# @Author: xiaoni
# @File  : loginGUI.py

import tkinter as tk
import json
from tkinter import scrolledtext, END

import main
from tkinter.scrolledtext import ScrolledText
import json
import random

from Credit import credit
from gragh import Gragh


class loginGUI():
    def __init__(self):
        self.window = tk.Toplevel()
        # 给窗口起一个标题
        self.window.title('课程管理系统')
        # 设定窗口大小(长x宽，这里是使用字符'x'而不是星号*)
        # self.window.geometry('600x370')

        self.canvas = tk.Canvas(self.window, height=370, width=600)  # 创建画布
        self.image_file1 = tk.PhotoImage(file='icon/backgroud.png')  # 加载图片文件
        self.image_file2 = tk.PhotoImage(file='icon/title1.png')  # 加载图片文件
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file1)  # 将图片置于画布上
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file2)  # 将图片置于画布上
        self.canvas.pack(side='top')  # 放置画布（为上端）

        img1 = tk.PhotoImage(file="icon/deepblue.png")
        img2 = tk.PhotoImage(file="icon/lightblue.png")
        img3 = tk.PhotoImage(file="icon/deepgreen.png")
        img4 = tk.PhotoImage(file="icon/lightgreen.png")
        img5 = tk.PhotoImage(file="icon/return.png")
        img6 = tk.PhotoImage(file="icon/normal_button.png")
        # 这里使用的是键值对（即属性: 值）的方式来设定参数，window表示该标签放置在window上，text为显示文本，bg(background)为背景颜色，
        # fg(fontground)为字体颜色，font=(字体, 字号)，width和height表示该标签的宽和高（如height为2表示该标签有2个字符那么高，这与字号的设定相关）
        '''
        img1 = tk.PhotoImage(file="image/01.png")
        button1 = tk.Button(win, text="Button1", image=img1, compound="center")
        目前支持 .png 与 .gif 格式， 还不支持 .jpg格式，Button的大小是根据图片的大小来确定的。
        我们使用Button传递数值时，需要用：lambda: 功能函数(var1, var2, ……)
        '''
        self.course_button1 = tk.Button(self.window, command=lambda: self.course_interface(1), text="大一上", width=110,
                                        height=22,
                                        cursor="hand2", relief="ridge", bd=1, image=img1, compound="center",
                                        font=("Consolas", 10))
        self.course_button2 = tk.Button(self.window, command=lambda: self.course_interface(2), text="大一下", width=110,
                                        height=22,
                                        cursor="hand2", relief="ridge", bd=1, image=img2, compound="center",
                                        font=("Consolas", 10))
        self.course_button3 = tk.Button(self.window, command=lambda: self.course_interface(3), text="大二上", width=110,
                                        height=22,
                                        cursor="hand2", relief="ridge", bd=1, image=img3, compound="center",
                                        font=("Consolas", 10))
        self.course_button4 = tk.Button(self.window, command=lambda: self.course_interface(4), text="大二下", width=110,
                                        height=22,
                                        cursor="hand2", relief="ridge", bd=1, image=img4, compound="center",
                                        font=("Consolas", 10))
        self.course_button5 = tk.Button(self.window, command=lambda: self.course_interface(5), text="大三上", width=110,
                                        height=22,
                                        cursor="hand2", relief="ridge", bd=1, image=img1, compound="center",
                                        font=("Consolas", 10))
        self.course_button6 = tk.Button(self.window, command=lambda: self.course_interface(6), text="大三下", width=110,
                                        height=22,
                                        cursor="hand2", relief="ridge", bd=1, image=img2, compound="center",
                                        font=("Consolas", 10))
        self.course_button7 = tk.Button(self.window, command=lambda: self.course_interface(7), text="大四上", width=110,
                                        height=22,
                                        cursor="hand2", relief="ridge", bd=1, image=img3, compound="center",
                                        font=("Consolas", 10))
        self.course_button8 = tk.Button(self.window, command=lambda: self.course_interface(8), text="大四下", width=110,
                                        height=22,
                                        cursor="hand2", relief="ridge", bd=1, image=img4, compound="center",
                                        font=("Consolas", 10))
        self.normal_button1 = tk.Button(self.window, command=self.go_back, width=20, height=20, cursor="hand2", bd=1,
                                        image=img5)
        self.normal_button2 = tk.Button(self.window, command=self.make_course, text="生成课表", width=50,
                                        height=18,
                                        cursor="hand2", relief="ridge", bd=1, image=img6, compound="center",
                                        font=("Consolas", 10))
        self.scr1 = scrolledtext.ScrolledText(self.window, width=16, height=5, font=("隶书", 10))
        self.scr2 = scrolledtext.ScrolledText(self.window, width=16, height=5, font=("隶书", 10))
        self.scr3 = scrolledtext.ScrolledText(self.window, width=16, height=5, font=("隶书", 10))
        self.scr4 = scrolledtext.ScrolledText(self.window, width=16, height=5, font=("隶书", 10))
        self.scr5 = scrolledtext.ScrolledText(self.window, width=16, height=5, font=("隶书", 10))
        self.scr6 = scrolledtext.ScrolledText(self.window, width=16, height=5, font=("隶书", 10))
        self.scr7 = scrolledtext.ScrolledText(self.window, width=16, height=5, font=("隶书", 10))
        self.scr8 = scrolledtext.ScrolledText(self.window, width=16, height=5, font=("隶书", 10))
        # self.scr1.insert(END, "计算机组成原理1") # 测试

        self.course_button1.place(x=10, y=65)
        self.course_button2.place(x=150, y=65)
        self.course_button3.place(x=290, y=65)
        self.course_button4.place(x=430, y=65)
        self.course_button5.place(x=10, y=205)
        self.course_button6.place(x=150, y=205)
        self.course_button7.place(x=290, y=205)
        self.course_button8.place(x=430, y=205)
        self.normal_button1.place(x=550, y=10)
        self.normal_button2.place(x=485, y=10)
        self.scr1.place(x=10, y=110)  # 滚动文本框在页面的位置
        self.scr2.place(x=150, y=110)
        self.scr3.place(x=290, y=110)
        self.scr4.place(x=430, y=110)
        self.scr5.place(x=10, y=250)
        self.scr6.place(x=150, y=250)
        self.scr7.place(x=290, y=250)
        self.scr8.place(x=430, y=250)

        # 主窗口循环显示

        # 居中显示
        width = 600
        height = 370
        screenwidth = self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.window.geometry(alignstr)
        # 大小不变
        self.window.resizable(0, 0)
        self.window.mainloop()

    # 使用Tk方法创建一个窗口，注意是大写T
    def course_interface(self, a):
        self.window.withdraw()
        self.window.quit()
        print(a)
        tk.messagebox.showinfo(title='课程管理系统', message='进入第一学期课表')

    def make_course(self):
        f = open(r"data\test.json", encoding='UTF-8')
        setting = json.load(f)

        getCreditSum = credit()
        print("continue")
        maxCreditSum = getCreditSum.x_int
        g = Gragh(setting, maxCreditSum)
        res = g.topoSort()

        self.restoChart(res)

    def restoChart(self, res):
        print("11111")
        for i in range(len(res)):
            if i == 0:
                scr = self.scr1
            elif i == 1:
                scr = self.scr2
            elif i == 2:
                scr = self.scr3
            elif i == 3:
                scr = self.scr4
            elif i == 4:
                scr = self.scr5
            elif i == 5:
                scr = self.scr6
            elif i == 6:
                scr = self.scr7
            for j in range(len(res[i])):
                if j == 0:
                    scr.insert(END, res[i][j])

                else:
                    scr.insert(END, "\n" + res[i][j])

    def refresh(self, i):
        print(i)

    def go_back(self):
        self.window.withdraw()
        main.main()


