#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/10/8 21:42
#@Author: xiaoni
#@File  : loginGUI.py

import tkinter as tk
import json

# 使用Tk方法创建一个窗口，注意是大写T
def verifyAccountData(account, password):

    # account=account[:-2]
    # password=password[:-2]
    f = open("data.json", encoding='UTF-8')  # 设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    setting = json.load(f)

    aaa=setting[0]['account'].ljust(10)


    for i in range(len(setting)):
        if setting[i]['account'].ljust(10)==account and setting[i]['password'].ljust(10)==password:
            if setting[i]['power']==1:
                return "master"
            if setting[i]['power']==0:
                return "user"
            break
        if setting[i]["account"].ljust(10)==account or setting[i]["password"].ljust(10)==password:
            return "noPassword"
            break
    return "noAccount"


def loginGUI():
    window = tk.Toplevel()
    # 给窗口起一个标题
    window.title('Tkinter is awesome')
    # 设定窗口大小(长x宽，这里是使用字符'x'而不是星号*)
    window.geometry('300x500')

    # 创建label控件
    label = tk.Label(window, text='Hello! Tkinter.', bg='black', fg='white', font=('Consolas', 12), width=30, height=2)
    # 这里使用的是键值对（即属性: 值）的方式来设定参数，window表示该标签放置在window上，text为显示文本，bg(background)为背景颜色，fg(fontground)为字体颜色，font=(字体, 字号)，width和height表示该标签的宽和高（如height为2表示该标签有2个字符那么高，这与字号的设定相关）

    # 将label放置
    label.pack()

    # 主窗口循环显示
    window.mainloop()