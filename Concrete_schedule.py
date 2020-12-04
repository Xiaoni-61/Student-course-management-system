#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/11/19 15:02
# @Author: xiaoni
# @File  : Concrete_schedule.py
import json
import random
import tkinter
from tkinter import ttk


class schedule:
    def __init__(self, courseNumber, res):
        self.courseNumber = courseNumber
        self.res = res
        self.relation_matrix_3d = [[[-1 for ii in range(2)] for ii in range(8)] for iii in range(5)]  # 创建临接矩阵
        self.nowCourseTime = []
        self.win = tkinter.Toplevel()
        self.win.title("第" + str(courseNumber) + "学期课表")  # #窗口标题
        self.win.iconbitmap("./icon/after.ico")
        # self.win.geometry("600x500+200+20")  # #窗口位置500后面是字母x
        '''
            Tab
        '''
        self.tab = ttk.Notebook(self.win)
        self.frame1 = tkinter.Frame(self.tab, bg="blue")
        self.tab.add(self.frame1, text="前八周")

        self.frame2 = tkinter.Frame(self.tab, bg="blue")
        self.tab.add(self.frame2, text="后八周")

        self.tab.pack(expand=True, fill=tkinter.BOTH)

        # 设置选中tab2
        # self.tab.select(self.frame1)
        '''
        表格
        '''
        self.tree1 = ttk.Treeview(self.frame1)  # #创建表格对象
        self.tree1["columns"] = ("星期一", "星期二", "星期三", "星期四", "星期五")  # #定义列

        self.tree1.column("星期一", width=130, anchor="center")  # #设置列
        self.tree1.column("星期二", width=130, anchor="center")
        self.tree1.column("星期三", width=130, anchor="center")
        self.tree1.column("星期四", width=130, anchor="center")
        self.tree1.column("星期五", width=130, anchor="center")
        self.tree1.heading("星期一", text="星期一")  # #设置显示的表头名
        self.tree1.heading("星期二", text="星期二")
        self.tree1.heading("星期三", text="星期三")
        self.tree1.heading("星期四", text="星期四")
        self.tree1.heading("星期五", text="星期五")

        # self.tree.insert("", 0, text="1", values=("卡恩", "18", "180", "65"))  # #给第0行添加数据，索引值可重复
        # self.tree.insert("", 1, text="2", values=("范冰冰", "38", "170", "55"))
        # self.tree.insert("", 2, text="3", values=("戚薇", "28", "169", "50"))
        # self.tree.insert("", 3, text="4", values=("杨霞", "30", "172", "63"))
        # self.tree.insert("", 4, text="中午", values=("", "", "", ""))
        # self.tree.insert("", 5, text="5", values=("迪丽热巴", "29", "175", "61"))
        # self.tree.insert("", 5, text="6", values=("迪丽热巴", "29", "175", "61"))
        # self.tree.insert("", 5, text="7", values=("迪丽热巴", "29", "175", "61"))
        # self.tree.insert("", 5, text="8", values=("迪丽热巴", "29", "175", "61"))

        self.courseRank()

        for i in range(8):
            self.tree1.insert("", i, text=str(i + 1), values=(("" if self.relation_matrix_3d[0][i][0] == -1 else
                                                              self.res[self.courseNumber - 1][
                                                                  self.relation_matrix_3d[0][i][0]]),
                                                             ("" if self.relation_matrix_3d[1][i][0] == -1 else
                                                              self.res[self.courseNumber - 1][
                                                                  self.relation_matrix_3d[1][i][0]]),
                                                             ("" if self.relation_matrix_3d[2][i][0] == -1 else
                                                              self.res[self.courseNumber - 1][
                                                                  self.relation_matrix_3d[2][i][0]]),
                                                             ("" if self.relation_matrix_3d[3][i][0] == -1 else
                                                              self.res[self.courseNumber - 1][
                                                                  self.relation_matrix_3d[3][i][0]]),
                                                             ("" if self.relation_matrix_3d[4][i][0] == -1 else
                                                              self.res[self.courseNumber - 1][
                                                                  self.relation_matrix_3d[4][i][0]])))



        self.tree = ttk.Treeview(self.frame2)  # #创建表格对象
        self.tree["columns"] = ("星期一", "星期二", "星期三", "星期四", "星期五")  # #定义列

        self.tree.column("星期一", width=130, anchor="center")  # #设置列
        self.tree.column("星期二", width=130, anchor="center")
        self.tree.column("星期三", width=130, anchor="center")
        self.tree.column("星期四", width=130, anchor="center")
        self.tree.column("星期五", width=130, anchor="center")
        self.tree.heading("星期一", text="星期一")  # #设置显示的表头名
        self.tree.heading("星期二", text="星期二")
        self.tree.heading("星期三", text="星期三")
        self.tree.heading("星期四", text="星期四")
        self.tree.heading("星期五", text="星期五")

        # self.tree.insert("", 0, text="1", values=("卡恩", "18", "180", "65"))  # #给第0行添加数据，索引值可重复
        # self.tree.insert("", 1, text="2", values=("范冰冰", "38", "170", "55"))
        # self.tree.insert("", 2, text="3", values=("戚薇", "28", "169", "50"))
        # self.tree.insert("", 3, text="4", values=("杨霞", "30", "172", "63"))
        # self.tree.insert("", 4, text="中午", values=("", "", "", ""))
        # self.tree.insert("", 5, text="5", values=("迪丽热巴", "29", "175", "61"))
        # self.tree.insert("", 5, text="6", values=("迪丽热巴", "29", "175", "61"))
        # self.tree.insert("", 5, text="7", values=("迪丽热巴", "29", "175", "61"))
        # self.tree.insert("", 5, text="8", values=("迪丽热巴", "29", "175", "61"))

        self.courseRank()

        for i in range(8):
            self.tree.insert("", i, text=str(i + 1), values=(("" if self.relation_matrix_3d[0][i][1] == -1 else
                                                              self.res[self.courseNumber - 1][
                                                                  self.relation_matrix_3d[0][i][1]]),
                                                             ("" if self.relation_matrix_3d[1][i][1] == -1 else
                                                              self.res[self.courseNumber - 1][
                                                                  self.relation_matrix_3d[1][i][1]]),
                                                             ("" if self.relation_matrix_3d[2][i][1] == -1 else
                                                              self.res[self.courseNumber - 1][
                                                                  self.relation_matrix_3d[2][i][1]]),
                                                             ("" if self.relation_matrix_3d[3][i][1] == -1 else
                                                              self.res[self.courseNumber - 1][
                                                                  self.relation_matrix_3d[3][i][1]]),
                                                             ("" if self.relation_matrix_3d[4][i][1] == -1 else
                                                              self.res[self.courseNumber - 1][
                                                                  self.relation_matrix_3d[4][i][1]])))
        print(res)
        self.tree1.pack()
        self.tree.pack()

        width = 1000
        height = 300
        screenwidth = self.win.winfo_screenwidth()
        screenheight = self.win.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.win.geometry(alignstr)
        # 大小不变
        self.win.resizable(0, 0)
        self.win.mainloop()

    def courseRank(self):

        while len(self.res) < 8:
            aa = []
            self.res.append(aa)

        ff = open(r".\data\course.json", encoding='UTF-8')
        setting1 = json.load(ff)

        for i in range(len(self.res[self.courseNumber - 1])):
            for j in range(len(setting1)):
                if self.res[self.courseNumber - 1][i] == setting1[j]["course"]:
                    credit = setting1[j]["credit"]
                    credit_int = int(credit)

                    self.randomCourse(i, credit_int)  # 开始随机

        for i in range(len(self.nowCourseTime)):
            for j in range(len(self.nowCourseTime[i])):
                self.relation_matrix_3d[self.nowCourseTime[i][j][0]][self.nowCourseTime[i][j][1]][
                    self.nowCourseTime[i][j][2]] = i

        print("111")

    def randomCourse(self, num, credit):
        temp = []
        for ii in range(len(self.nowCourseTime)):
            for jj in range(len(self.nowCourseTime[ii])):
                temp.append(self.nowCourseTime[ii][jj])

        self.nowCourseTime.append([])
        for i in range(credit):
            day_in_week = random.randint(0, 4)
            time_in_day = random.randint(0, 7)
            eight_or_sixteen = random.randint(0, 1)
            while [day_in_week, time_in_day, eight_or_sixteen] in temp:
                day_in_week = random.randint(0, 4)
                time_in_day = random.randint(0, 7)
                eight_or_sixteen = random.randint(0, 1)
            self.nowCourseTime[num].append([day_in_week, time_in_day, eight_or_sixteen])
