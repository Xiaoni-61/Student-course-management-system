#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/11/15 11:55
# @Author: xiaoni
# @File  : gragh.py
import json
import random


class Gragh():
    # def __init__(self):
    #     self.v = []
    #     self.e = []

    # 初始化
    def __init__(self, setting, maxCreditSum):
        self.v = []
        self.e = []
        self.res = []
        self.resBackUp = []
        self.maxCreditSum = maxCreditSum
        for i in range(len(setting)):
            flag1 = 0
            flag2 = 0
            for j in range(len(self.v)):
                if self.v[j] == setting[i]['CName']:
                    flag1 = 1

                if self.v[j] == setting[i]['toName']:
                    flag2 = 1

                if self.v[j] == setting[i]['CName'] and self.v[j] == setting[i]['toName']:
                    flag1 = 1
                    flag2 = 1
            if flag1 == 0:
                self.v.append(setting[i]['CName'])
            if flag2 == 0:
                self.v.append(setting[i]['toName'])

        # 建边
        for i in range(len(setting)):
            ee = []
            ee.append(setting[i]['CName'])
            ee.append(setting[i]['toName'])
            self.e.append(ee)

        self.member_dict = {"近代史": 0, "思修": 1, "毛概": 2, "马原": 3, "大学英语": 4, "高级英语": 5,
                            "高级英语阅读": 6, "体育1": 7, "体育2": 8, "体育3": 9, "体育4": 10, "高数1": 11, "大物1": 12, "大物2": 13,
                            "大物实验1": 14,
                            "大物实验2": 15, "电路与电子技术": 16, "电子与电子技术实验": 17, "高数2": 18, "集合与图论": 19, "代数与逻辑": 20,
                            "数据结构与算法": 21,
                            "线性代数": 22, "概率论与数理方程": 23, "物联网工程导论": 24, "算法设计与分析": 25, "数字逻辑": 26, "数字逻辑实验": 27,
                            "计算机组成原理": 28,
                            "计算机组成原理课设": 29, "计算机系统结构": 30, "计算机网络": 31, "操作系统": 32, "高级语言程序设计": 33, "高级语言程序设计课设": 34,
                            "面向对象程序设计": 35,
                            "汇编语言程序设计": 36, "单片机原理与技术": 37, "嵌入式系统": 38, "无线传感器网络": 39, "无线传感器网络课设": 40, "嵌入式技术课设": 41,
                            "编译原理": 42,
                            "微型计算机接口": 43, "RFID技术": 44, "数据库原理": 45, "数据结构与算法课设": 46, "软件工程引论": 47, "软件类综合课设": 48,
                            "计算机网络课设": 49,
                            "物联网感知课设": 50, "物联网工程实践课设": 51
                            }
        self.member_dict2 = ["近代史", "思修", "毛概", "马原", "大学英语", "高级英语",
                             "高级英语阅读", "体育1", "体育2", "体育3", "体育4", "高数1", "大物1", "大物2", "大物实验1",
                             "大物实验2", "电路与电子技术", "电子与电子技术实验", "高数2", "集合与图论", "代数与逻辑", "数据结构与算法",
                             "线性代数", "概率论与数理方程", "物联网工程导论", "算法设计与分析", "数字逻辑", "数字逻辑实验", "计算机组成原理",
                             "计算机组成原理课设", "计算机系统结构", "计算机网络", "操作系统", "高级语言程序设计", "高级语言程序设计课设", "面向对象程序设计",
                             "汇编语言程序设计", "单片机原理与技术", "嵌入式系统", "无线传感器网络", "无线传感器网络课设", "嵌入式技术课设", "编译原理",
                             "微型计算机接口", "RFID技术", "数据库原理", "数据结构与算法课设", "软件工程引论", "软件类综合课设", "计算机网络课设",
                             "物联网感知课设", "物联网工程实践课设"
                             ]
        # 构建临接矩阵
        self.relation_matrix = [[0 for ii in range(len(self.v))] for ii in range(len(self.v))]  # 创建临接矩阵
        for (x, y) in self.e:
            x_index = self.member_dict[x]
            y_index = self.member_dict[y]
            self.relation_matrix[x_index][y_index] = 1

        # print(self.relation_matrix)

    # 构造总课程json 第一次使用时创建course的json文件 初始化学分
    def create_course(self):
        course = self.v
        setting = []
        for i in range(len(course)):
            test_dict = {
                "course": course[i],
                "credit": 0
            }
            setting.append(test_dict)

        with open(r".\data\course.json", 'w', encoding='UTF-8') as fw:
            json.dump(setting, fw, ensure_ascii=False, indent=4)

    # 计算总学分
    def calculate_credit(self):
        ff = open(r".\data\course.json", encoding='UTF-8')
        setting1 = json.load(ff)
        self.credit_sum = 0
        for i in range(len(setting1)):
            self.credit_sum = self.credit_sum + setting1[i]["credit"]

    '''
    调整课程顺序（向前或是向后）
    course为课程名 courseAddress为相对现在位置的相对位置
    返回调整后的总学期课表
    '''

    def adjustcourse(self, course, courseAddress):
        self.resBackUp = self.res
        # 备份res（每学期课程数据）
        for i in range(len(self.res)):
            if course in self.res[i]:
                j = i
                break

        nowCourseArray = []
        nowCourseArray.append(self.member_dict[course])
        jjj = 0
        courseID = self.member_dict[course]
        while True:
            for i in range(len(self.relation_matrix[courseID])):
                if self.relation_matrix[courseID][i] == 1:
                    nowCourseArray.append(i)
            jjj += 1
            try:
                courseID = nowCourseArray[jjj]
            except IndexError:
                if jjj == len(nowCourseArray):
                    break
        if courseAddress > 0:
            for i in range(len(nowCourseArray)):
                for jj in range((len(self.res) - 1), -1, -1):
                    if self.member_dict2[nowCourseArray[i]] in self.res[jj]:
                        self.res[jj].remove(self.member_dict2[nowCourseArray[i]])
                        try:
                            if (jj + courseAddress) > 7:
                                self.res = self.resBackUp  # 恢复数据
                                return False
                            self.res[jj + courseAddress].append(self.member_dict2[nowCourseArray[i]])
                        except IndexError:
                            aa = []
                            self.res.append(aa)
                            self.res[jj + courseAddress].append(self.member_dict2[nowCourseArray[i]])
        if courseAddress < 0:
            nowPreCourseArray = []
            for i in range(len(self.relation_matrix[courseID])):
                if self.relation_matrix[i][nowCourseArray[0]] == 1:
                    nowPreCourseArray.append(i)

            for i in range(len(nowPreCourseArray)):
                if self.member_dict2[nowPreCourseArray[i]] in self.res[j + courseAddress]:
                    return False

            for i in range(len(nowCourseArray)):
                for jj in range(len(self.res)):
                    if self.member_dict2[nowCourseArray[i]] in self.res[jj]:
                        self.res[jj].remove(self.member_dict2[nowCourseArray[i]])
                        if (jj + courseAddress) < 0:
                            self.res = self.resBackUp
                            return False
                        else:
                            self.res[jj + courseAddress].append(self.member_dict2[nowCourseArray[i]])

        return self.res

    '''
        设定每学期修的学分最大值
        若多于设定值则随机删除某节课 直到满足条件
    '''

    def rank_again(self, a):
        f = open(r".\data\course.json", encoding='UTF-8')
        setting = json.load(f)
        if len(a) == 1:
            return a
        while True:
            sum_score = 0
            for i in range(len(a)):
                for j in range(len(setting)):
                    if a[i] == setting[j]["course"]:
                        sum_score = sum_score + setting[j]["credit"]
            if sum_score <= self.maxCreditSum:
                return a
            elif sum_score > self.maxCreditSum:
                b = random.randint(0, len(a) - 1)
                a.remove(a[b])

    # 现阶段入度为0的点
    def indegree0(self):
        if not self.v:
            return None
        tmp = self.v[:]
        for i in self.e:
            if i[1] in tmp:
                tmp.remove(i[1])
        if not tmp:
            return -1

        tmp = self.rank_again(tmp)

        for t in tmp:
            for i in range(len(self.e)):
                if t in self.e[i]:
                    self.e[i] = 'toDel'  # 占位，之后删掉
        if self.e:  # 删除重复元素
            for r in range(len(self.e) - 1, -1, -1):
                # 作比较
                for c in range(r):
                    if self.e[r] == self.e[c]:
                        self.e.remove(self.e[r])
                        break  # 如果删除了后面元素,则无需继续用当前元素比较了

            self.e.remove('toDel')
            self.e[:] = list(self.e)
        if self.v:
            for t in tmp:
                self.v.remove(t)
        return tmp

    '''
        拓扑排序开始！
    '''

    def topoSort(self):
        self.res = []
        while True:
            nodes = self.indegree0()
            if nodes is None:
                break
            if nodes == -1:
                print('there\'s a circle.')
                return None
            self.res.append(nodes)  # extend 是直接组合  append是列表再组合
        return self.res

# f = open(r".\data\test.json", encoding='UTF-8')
# setting = json.load(f)
# tab1 = 1
# g = Gragh(setting)
