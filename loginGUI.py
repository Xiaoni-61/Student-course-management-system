#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/10/8 21:42
# @Author: xiaoni
# @File  : loginGUI.py

import tkinter as tk
import json
from tkinter import scrolledtext, END
from tkinter.scrolledtext import ScrolledText
import json
import random
from gragh import Gragh


class loginGUI():
    def __init__(self):
        self.window = tk.Toplevel()
        # 给窗口起一个标题
        self.window.title('Tkinter is awesome')
        # 设定窗口大小(长x宽，这里是使用字符'x'而不是星号*)
        self.window.geometry('600x370')

        # 创建label控件
        self.label = tk.Label(self.window, text='大学四年总课表', bg='blue', fg='white', font=('Consolas', 15), width=35,
                              height=2)
        # 这里使用的是键值对（即属性: 值）的方式来设定参数，window表示该标签放置在window上，text为显示文本，bg(background)为背景颜色，
        # fg(fontground)为字体颜色，font=(字体, 字号)，width和height表示该标签的宽和高（如height为2表示该标签有2个字符那么高，这与字号的设定相关）
        '''
        img1 = tk.PhotoImage(file="image/01.png")
        button1 = tk.Button(win, text="Button1", image=img1, compound="center")
        目前支持 .png 与 .gif 格式， 还不支持 .jpg格式，Button的大小是根据图片的大小来确定的。
        我们使用Button传递数值时，需要用：lambda: 功能函数(var1, var2, ……)
        '''
        self.course_button1 = tk.Button(self.window, command=lambda: self.course_interface(1), text="大一上", width=16,
                                        cursor="hand2", relief="ridge", bd=1)
        self.course_button2 = tk.Button(self.window, command=lambda: self.course_interface(1), text="大一下", width=16,
                                        cursor="hand2", relief="ridge", bd=1)
        self.course_button3 = tk.Button(self.window, command=lambda: self.course_interface(1), text="大二上", width=16,
                                        cursor="hand2", relief="ridge", bd=1)
        self.course_button4 = tk.Button(self.window, command=lambda: self.course_interface(1), text="大二下", width=16,
                                        cursor="hand2", relief="ridge", bd=1)
        self.course_button5 = tk.Button(self.window, command=lambda: self.course_interface(1), text="大三上", width=16,
                                        cursor="hand2", relief="ridge", bd=1)
        self.course_button6 = tk.Button(self.window, command=lambda: self.course_interface(1), text="大三下", width=16,
                                        cursor="hand2", relief="ridge", bd=1)
        self.course_button7 = tk.Button(self.window, command=lambda: self.course_interface(1), text="大四上", width=16,
                                        cursor="hand2", relief="ridge", bd=1)
        self.course_button8 = tk.Button(self.window, command=lambda: self.course_interface(1), text="大四下", width=16,
                                        cursor="hand2", relief="ridge", bd=1)
        self.scr1 = scrolledtext.ScrolledText(self.window, width=16, height=5, font=("隶书", 10))
        self.scr2 = scrolledtext.ScrolledText(self.window, width=16, height=5, font=("隶书", 10))
        self.scr3 = scrolledtext.ScrolledText(self.window, width=16, height=5, font=("隶书", 10))
        self.scr4 = scrolledtext.ScrolledText(self.window, width=16, height=5, font=("隶书", 10))
        self.scr5 = scrolledtext.ScrolledText(self.window, width=16, height=5, font=("隶书", 10))
        self.scr6 = scrolledtext.ScrolledText(self.window, width=16, height=5, font=("隶书", 10))
        self.scr7 = scrolledtext.ScrolledText(self.window, width=16, height=5, font=("隶书", 10))
        self.scr8 = scrolledtext.ScrolledText(self.window, width=16, height=5, font=("隶书", 10))
        self.scr1.insert(END, "计算机组成原理1")
        self.scr1.insert(END, "\n计算机组成原理2")
        self.scr1.insert(END, "\n计算机组成原理3")
        self.scr1.insert(END, "\n计算机组成原理4")
        self.scr1.insert(END, "\n计算机组成原理5")
        self.scr1.insert(END, "\n计算机组成原理5")
        self.scr1.insert(END, "\n计算机组成原理5")
        self.course_button1.place(x=10, y=60)
        self.course_button2.place(x=150, y=60)
        self.course_button3.place(x=290, y=60)
        self.course_button4.place(x=430, y=60)
        self.course_button5.place(x=10,  y=200)
        self.course_button6.place(x=150, y=200)
        self.course_button7.place(x=290, y=200)
        self.course_button8.place(x=430, y=200)
        self.scr1.place(x=10, y=105)  # 滚动文本框在页面的位置
        self.scr2.place(x=150, y=105)
        self.scr3.place(x=290, y=105)
        self.scr4.place(x=430, y=105)
        self.scr5.place(x=10,  y=245)
        self.scr6.place(x=150, y=245)
        self.scr7.place(x=290, y=245)
        self.scr8.place(x=430, y=245)

        # 将label放置
        self.label.pack()

        # 主窗口循环显示
        self.window.mainloop()

    # 使用Tk方法创建一个窗口，注意是大写T
    def course_interface(self, a):
        self.window.withdraw()
        self.window.quit()
        print(a)
        tk.messagebox.showinfo(title='课程管理系统', message='进入第一学期课表')
