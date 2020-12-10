#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/10/8 22:25
# @Author: xiaoni
# @File  : signupGUI.py
import tkinter
import tkinter as tk

import json
import main
from tkinter import messagebox, END


class signup():

    def __init__(self):
        self.window = tk.Toplevel()
        self.window.iconbitmap("./icon/first.ico")

        self.canvas = tkinter.Canvas(self.window, height=500, width=500)  # 创建画布
        self.image_file = tkinter.PhotoImage(file=r'icon\abc.gif')  # 加载图片文件
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)  # 将图片置于画布上
        self.canvas.pack(side='top')  # 放置画布（为上端）

        self.window.title('注册界面')
        self.window.iconbitmap("./icon/after.ico")
        self.window.geometry('450x300')

        self.label_account = tkinter.Label(self.window, text='Account: ')
        self.label_password = tkinter.Label(self.window, text='Password: ')
        self.label_password_again = tkinter.Label(self.window, text='Password Aagin: ')

        # 创建一个账号输入框,并设置尺寸
        self.input_account = tkinter.Entry(self.window, width=30)
        # 创建一个密码输入框,并设置尺寸
        self.input_password = tkinter.Entry(self.window, show='*', width=30)
        self.input_password_again = tkinter.Entry(self.window, show='*', width=30)

        # 创建一个登录系统的按钮
        self.signup_finish_button = tkinter.Button(self.window, command=self.signup_finish, text="finish", width=10)
        # 创建一个注册系统的按钮
        self.go_back_button = tkinter.Button(self.window, command=self.go_back, text="go back", width=10)

        self.label_account.place(x=76, y=150)
        self.label_password.place(x=67, y=175)
        self.label_password_again.place(x=30, y=200)

        self.input_account.place(x=135, y=150)
        self.input_password.place(x=135, y=175)
        self.input_password_again.place(x=135, y=200)

        self.signup_finish_button.place(x=140, y=235)
        self.go_back_button.place(x=240, y=235)

        width = 450
        height = 300
        screenwidth = self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.window.geometry(alignstr)
        # 主窗口循环显示
        self.window.mainloop()

    def signup_finish(self):
        f = open(r".\data\data.json", encoding='UTF-8')
        setting = json.load(f)
        flag = 1
        account = self.input_account.get().ljust(10, " ")
        password = self.input_password.get().ljust(10, " ")
        password_again = self.input_password_again.get().ljust(10, " ")

        if password != password_again:
            tkinter.messagebox.showinfo(title='课程管理系统', message='两次输入密码不一致!')
            self.input_password.delete(0, END)
            self.input_password_again.delete(0, END)
        else:
            for i in range(len(setting)):
                if setting[i]['account'].ljust(10) == account:
                    tkinter.messagebox.showinfo(title='课程管理系统', message='输入账号已存在!')
                    flag = 0
                    self.input_account.delete(0, END)
                    self.input_password.delete(0, END)
                    self.input_password_again.delete(0, END)
                    break

            test_dict = {
                "account": account,
                "password": password,
                "power": 0,
                "course": [],
                "g": []
            }
            if flag == 1:
                setting.append(test_dict)
                tkinter.messagebox.showinfo(title='课程管理系统', message='注册成功!')
                self.input_account.delete(0, END)
                self.input_password.delete(0, END)
                self.input_password_again.delete(0, END)

            with open(r".\data\data.json", 'w') as fw:
                json.dump(setting, fw)

            self.window.withdraw()
            main.main()

    def go_back(self):
        self.window.withdraw()
        main.main()
