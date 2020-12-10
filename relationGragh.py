#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 4/12/2020 下午 9:06
# @Author: xiaoni
# @File  : relationGragh.py
import tkinter as tk
import json
from tkinter import scrolledtext, END


class relationGragh:

    def __init__(self, res):
        self.res = res
        self.falseOrTrue = 0
        self.root2 = tk.Toplevel()
        self.root2.title("课程管理系统")
        self.root2.iconbitmap("./icon/after.ico")

        self.canvas = tk.Canvas(self.root2, width=1600, height=550, background="white")
        self.canvas.place(x=0, y=50)
        img1 = tk.PhotoImage(file="icon/relation.png")
        img2 = tk.PhotoImage(file="icon/return.png")
        # tk.Label(self.root2, text="高数").place(x=500, y=500)

        self.canvas.create_line(180, 0, 180, 550, dash=(4, 4))
        self.canvas.create_line(360, 0, 360, 550, dash=(4, 4))
        self.canvas.create_line(540, 0, 540, 550, dash=(4, 4))
        self.canvas.create_line(720, 0, 720, 550, dash=(4, 4))
        self.canvas.create_line(900, 0, 900, 550, dash=(4, 4))
        self.canvas.create_line(1080, 0, 1080, 550, dash=(4, 4))
        self.canvas.create_line(1260, 0, 1260, 550, dash=(4, 4))
        for i in range(8):
            tk.Label(self.root2, fg="light green", bg="dark green", bd=10, text='第' + str(i + 1) + '学期').place(
                x=i * 180 + 55,
                y=0)

        self.normal_button = tk.Button(self.root2, command=self.display_relation, width=25,
                                       height=25,
                                       cursor="hand2", relief="flat", bd=0, image=img1)
        self.normal_button2 = tk.Button(self.root2, command=self.goback, width=25,
                                        height=25,
                                        cursor="hand2", relief="flat", bd=0, image=img2)

        self.normal_button.place(x=5, y=10)
        self.normal_button2.place(x=1395, y=10)

        # canvas.create_rectangle(0, 0, 100, 200, fill='green')
        self.color = 'red'
        for i in range(len(self.res)):
            for j in range(len(self.res[i])):
                if i == 0:
                    self.color = 'green'
                elif i == 1:
                    self.color = 'red'
                elif i == 2:
                    self.color = 'blue'
                elif i == 3:
                    self.color = 'orange'
                elif i == 4:
                    self.color = 'yellow'
                elif i == 5:
                    self.color = 'pink'
                elif i == 6:
                    self.color = 'purple'
                elif i == 7:
                    self.color = 'cyan'

                self.canvas.create_rectangle(i * 180 + 25, j * 50 + 10, i * 180 + 150, j * 50 + 40, fill=self.color)
                tk.Label(self.root2, text=self.res[i][j]).place(x=i * 180 + 35, y=j * 50 + 65)
                # canvas.create_text(x=i * 200 + 30, y=j * 50 + 60, text=self.res[i][j])
        # 居中显示
        width = 1440
        height = 600
        screenwidth = self.root2.winfo_screenwidth()
        screenheight = self.root2.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root2.geometry(alignstr)
        # 大小不变
        self.root2.resizable(0, 0)

        self.root2.mainloop()

    def display_relation(self):
        self.falseOrTrue += 1
        startX = 0  # 划线的四个坐标
        startY = 0
        endX = 0
        endY = 0
        f = open(r"data\test.json", encoding='UTF-8')
        setting = json.load(f)
        for ii in range(len(setting)):
            for i in range(len(self.res)):
                for j in range(len(self.res[i])):
                    if self.res[i][j] == setting[ii]["CName"]:
                        startX = i * 180 + 150
                        startY = j * 50 + 25
                    if self.res[i][j] == setting[ii]["toName"]:
                        endX = i * 180 + 25
                        endY = j * 50 + 25
            if (self.falseOrTrue % 2) == 1:
                self.canvas.create_line(startX, startY, endX, endY, arrow=tk.LAST, fill='black')
            else:
                self.canvas.create_line(startX, startY, endX, endY, arrow=tk.LAST, fill="white")

        pass

    def goback(self):
        self.root2.withdraw()
