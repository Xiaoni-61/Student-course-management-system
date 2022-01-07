#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/9/25 15:04
# @Author: xiaoni
# @File  : main.py


# 这是系统的登录界面
import json
import tkinter
import loginGUI, signupGUI
from tkinter import messagebox, END


class Login(object):
    def __init__(self):
        # 创建主窗口,用于容纳其它组件
        self.root = tkinter.Toplevel()
        # 给主窗口设置标题内容
        self.root.title("课程管理系统")
        self.root.iconbitmap("./icon/first.ico")
        # self.root.geometry('450x300')
        # 运行代码时记得添加一个gif图片文件，不然是会出错的
        self.canvas = tkinter.Canvas(self.root, height=500, width=500)  # 创建画布
        self.image_file = tkinter.PhotoImage(file=r'icon\abc.gif')  # 加载图片文件
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)  # 将图片置于画布上
        self.canvas.pack(side='top')  # 放置画布（为上端）

        # 创建一个`label`名为`Account: `
        self.label_account = tkinter.Label(self.root, text='Account: ')
        # 创建一个`label`名为`Password: `
        self.label_password = tkinter.Label(self.root, text='Password: ')

        # 创建一个账号输入框,并设置尺寸
        self.input_account = tkinter.Entry(self.root, width=30)
        # 创建一个密码输入框,并设置尺寸
        self.input_password = tkinter.Entry(self.root, show='*', width=30)

        # 创建一个登录系统的按钮
        self.login_button = tkinter.Button(self.root, command=self.backstage_interface, text="Login", width=10)
        # 创建一个注册系统的按钮
        self.siginUp_button = tkinter.Button(self.root, command=self.siginUp_interface, text="Sign up", width=10)

        # 居中显示
        width = 450
        height = 300
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        # 窗口大小不变
        self.root.resizable(0, 0)

    def gui_arrang(self):
        self.label_account.place(x=60, y=170)
        self.label_password.place(x=60, y=195)
        self.input_account.place(x=135, y=170)
        self.input_password.place(x=135, y=195)
        self.login_button.place(x=140, y=235)
        self.siginUp_button.place(x=240, y=235)

        # 进入注册界面

    def siginUp_interface(self):
        self.root.withdraw()
        self.root.quit()
        tkinter.messagebox.showinfo(title='课程管理系统', message='进入注册界面')
        signupGUI.signup()

        # 进行登录信息验证

    def backstage_interface(self):
        account = self.input_account.get().ljust(10, " ")
        password = self.input_password.get().ljust(10, " ")
        # 对账户信息进行验证，普通用户返回user，管理员返回master，账户错误返回noAccount，密码错误返回noPassword

        verifyResult = self.verifyAccountData(account, password)

        if verifyResult == 'master':
            self.root.withdraw()
            # tkinter.messagebox.showinfo(title='课程管理系统', message='进入管理界面')
            loginGUI.loginGUI(account)
        elif verifyResult == 'user':
            self.root.withdraw()
            # tkinter.messagebox.showinfo(title='课程管理系统', message='进入用户界面')
            loginGUI.loginGUI(account)
        elif verifyResult == 'noAccount':
            tkinter.messagebox.showinfo(title='课程管理系统', message='该账号不存在请重新输入!')
            self.input_account.delete(0, END)
            self.input_password.delete(0, END)
        elif verifyResult == 'noPassword':
            tkinter.messagebox.showinfo(title='课程管理系统', message='账号/密码错误请重新输入!')
            self.input_account.delete(0, END)
            self.input_password.delete(0, END)

    def rootagain(self):
        self.root.deiconify()

    def verifyAccountData(self, account, password):
        # account=account[:-2]
        # password=password[:-2]
        f = open(r".\data\data.json", encoding='UTF-8')
        setting = json.load(f)

        aaa = setting[0]['account'].ljust(10)

        for i in range(len(setting)):
            if setting[i]['account'].ljust(10) == account and setting[i]['password'].ljust(10) == password:
                return "user"
            if setting[i]["account"].ljust(10) == account and setting[i]["password"].ljust(10) != password:
                return "noPassword"
        return "noAccount"


def main():
    # 初始化对象
    L = Login()
    # 进行布局
    L.gui_arrang()
    # 主程序执行
    tkinter.mainloop()


if __name__ == '__main__':
    main()

