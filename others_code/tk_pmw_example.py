#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'


import sys
import os
import time

import Pmw
from tkinter import *
from tkinter.messagebox import *


global number_OrgAddr, number_DestAddr, count

number_OrgAddr, number_DestAddr, count = 0, 0, 0


class GUIFrame(Frame):
    """ Demonstrate Entrys and Envent Building"""

    File_Count = 0
    first = Init_FileCount = "prm20080610_01011000000.unl"
    Init_FileCount_Postfix = ".unl"
    # File_Path = os.getcwd()
    File_Path = "D://bill//test//"
    # Begin_No 为话单文件ID初始化序号
    Begin_No = 1
    Begin_No = "%030d" % Begin_No

    print("File_Path=", File_Path)

    def __init__(self, parent):

        Frame.__init__(self)

        self.pack(expand=YES, fill=BOTH)

        self.master.title("短消息监控模拟器V1.0发布")

        self.master.geometry("700x500-20+20")  # width X length

        self.master.resizable(width=False, height=False)

        # Frame1

        self.frame1 = Frame(self)

        self.frame1.pack(pady=5)  # 垂直间距

        # 文件名输入

        self.label1 = Label(self.frame1, font="Tahoma 10", text="文件名:")

        # self.spacelabel = Label(self.frame1, width =15)

        print(self.File_Count)

        self.text1 = Entry(self.frame1, name='text1', width=70)

        self.text1.insert(INSERT, self.Init_FileCount)

        self.button2 = Button(self.frame1, text="增加数量", font="Toahoma 10", command=self.addCount)

        self.text1.bind("<Return>", self.showContents)

        self.label1.pack(side=LEFT, padx=5)

        self.text1.pack(side=LEFT, padx=2)

        self.button2.pack(side=LEFT, padx=5)

        # 记录数

        self.label2 = Label(self.frame1, font="Tahoma 10", text="记录数:", width=10)

        self.text2 = Entry(self.frame1)

        self.text2.insert(INSERT, "1")

        #        self.text2.insert(INSERT, "Enter text here")

        self.text2.bind("<Return>", self.showContents)

        #        self.spacelabel.pack(side=LEFT,padx=5)

        self.label2.pack(side=LEFT, padx=5)

        self.text2.pack(side=LEFT, padx=2)

        # Frame2

        # 开始文件数

        self.frame2 = Frame(self)

        self.frame2.pack(pady=10)

        self.spacelabel1 = Label(self.frame2, width=9)

        self.label3 = Label(self.frame2, font="Toahoma 10", text="开始文件数:")

        self.text3 = Entry(self.frame2)

        self.text3.insert(INSERT, "1")

        self.label3.pack(side=LEFT, padx=5)

        self.text3.pack(side=LEFT, padx=2)

        # 生成文件数

        self.label4 = Label(self.frame2, font="Toahoma 10", text="生成文件数:")

        self.text4 = Entry(self.frame2)

        self.text4.bind("<Return>", self.showContents)

        self.text4.insert(INSERT, "1")

        self.label4.pack(side=LEFT, padx=5)

        self.text4.pack(side=LEFT, padx=5)

        # 文件时间间隔

        self.label5 = Label(self.frame2, font="Toahoma 10", text="文件间隔时间:")

        self.label11 = Label(self.frame2, font="Toahoma 10", text="毫秒")

        self.text5 = Entry(self.frame2, width=7)

        self.text5.insert(INSERT, "0")

        self.text5.bind("<Return>", self.showContents)

        self.spacelabel1.pack(side=LEFT, padx=5)

        self.label5.pack(side=LEFT, padx=5)

        self.text5.pack(side=LEFT, padx=5)

        self.label11.pack(side=LEFT)

        # Frame3

        # 主叫号码

        self.frame3 = Frame(self)

        self.frame3.pack(pady=10)

        self.spacelabel2 = Label(self.frame3, width=30)

        self.label6 = Label(self.frame3, font="Toahoma 10", text="主叫号码:")

        self.text6 = Entry(self.frame3, name="text6", width=30)

        self.text6.insert(INSERT, "8613330980570")

        self.text6.bind("<Return>", self.showContents)

        self.label6.pack(side=LEFT, padx=5)

        self.text6.pack(side=LEFT, padx=2)

        # 主叫号码步长

        self.label7 = Label(self.frame3, font="Toahoma 10", text="主叫步长:")

        self.text7 = Entry(self.frame3, name="text7", width=10)

        self.text7.bind("<Return>", self.showContents)

        self.text7.insert(INSERT, "0")

        self.spacelabel2.pack(side=LEFT)

        self.label6.pack(side=LEFT, padx=5)

        self.label7.pack(side=LEFT, padx=5)

        self.text7.pack(side=LEFT, padx=2)

        # 提交按钮

        self.submitButton = Button(self.frame3, text="确定", font="Toahoma 10", command=self.submitButton)

        self.submitButton.bind("<Enter>", self.rolloverEnter)  # 鼠标事件:进入

        self.submitButton.bind("<Leave>", self.rolloverLeave)  # 鼠标事件：离开

        self.spacelabel2.pack(side=LEFT, padx=5)

        self.submitButton.pack(side=LEFT, padx=28)

        # Frame4

        # 被叫号码

        self.frame4 = Frame(self)

        self.frame4.pack(pady=10)

        self.spacelabel2 = Label(self.frame4, width=30)

        self.label8 = Label(self.frame4, font="Toahoma 10", text="被叫号码:")

        self.text8 = Entry(self.frame4, name="text6", width=30)

        self.text8.insert(INSERT, "8613230980570")

        self.text8.bind("<Return>", self.showContents)

        self.label8.pack(side=LEFT, padx=5)

        self.text8.pack(side=LEFT, padx=2)

        # 被叫号码步长

        self.label9 = Label(self.frame4, font="Toahoma 10", text="被叫步长:")

        self.text9 = Entry(self.frame4, name="text7", width=10)

        self.text9.bind("<Return>", self.showContents)

        self.text9.insert(INSERT, "0")

        self.spacelabel2.pack(side=LEFT)

        self.label9.pack(side=LEFT, padx=5)

        self.label9.pack(side=LEFT, padx=5)

        self.text9.pack(side=LEFT, padx=2)

        # 提交按钮

        self.ExitButton = Button(self.frame4, text="退出", font="Toahoma 10",

                                 command=self.ExitButton)

        self.ExitButton.bind("<Enter>", self.rolloverEnter)  # 鼠标事件:进入

        self.ExitButton.bind("<Leave>", self.rolloverLeave)  # 鼠标事件：离开

        self.spacelabel2.pack(side=LEFT, padx=5)

        self.ExitButton.pack(side=LEFT, padx=28)

        # Frame5

        # 时间区域

        self.frame5 = Frame(self)

        self.frame5.pack(pady=10)

        # 本地时间

        self.spacelabel3 = Label(self.frame5, width=30)

        self.localtimeLab = Label(self.frame5, text="是否使用本地时间:", font="Toahoma 10")

        self.chooseTime = BooleanVar()

        self.localtimeCheck = Checkbutton(self.frame5, variable=self.chooseTime,

                                          font="Toahoma 10", command=self.decideLocaltime)

        self.localtimeLab.pack(side=LEFT, padx=3)

        self.localtimeCheck.pack(side=LEFT, padx=3)

        # 时间控件

        # 开始时间

        self.startLab = Label(self.frame5, text="手工选择开始时间:", font="Toahoma 10")

        self.spacelabel3.pack(side=LEFT)

        self.startLab.pack(side=LEFT, padx=3)

        # Need to use long ints here because on the Macintosh the maximum size

        # of an integer is smaller than the value returned by time.time().

        now = (time.time() / 300) * 300

        # Create the Counters.

        self._date = Pmw.Counter(self.frame5,
                                 labelpos='w',
                                 entryfield_value=
                                 time.strftime('%Y/%m/%d', time.localtime(now)),
                                 entry_width=10,
                                 entryfield_validate={'validator': 'date',
                                                      'separator': '/'},  # 'format': 'ymd',
                                 datatype={'counter': 'date', 'yyyy': 1,

                                           'separator': '/'}  # 'format': 'ymd',
                                 )

        self._date.pack(side=LEFT, padx=3)

        self._time = Pmw.Counter(self.frame5,
                                 labelpos='w',
                                 entry_width=10,
                                 entryfield_value=
                                 time.strftime('%H:%M:%S', time.localtime(now)),
                                 entryfield_validate={'validator': 'time',
                                                      'min': '00:00:00', 'max': '23:59:59',
                                                      'minstrict': 0, 'maxstrict': 0},
                                 datatype={'counter': 'time', 'time24': 1},

                                 increment=5 * 60)

        self._time.pack(side=LEFT, padx=3)

        # frame6

        # 消息内容

        self.frame6 = Frame(self)

        self.frame6.pack(pady=10)

        self.spacelabel4 = Label(self.frame6, width=5)

        self.contentLab = Label(self.frame6, text="消息内容:", font="Toahoma 10")

        self.contentLab.pack(side=LEFT, padx=3)

        self.historyText = Pmw.HistoryText(self.frame6,

                                           text_wrap='none',

                                           text_width=77,

                                           text_height=10,

                                           )

        self.historyText.pack(side=LEFT)

        self.historyText.component('text').focus()

        self.countText = Button(self.frame6, text="计算", font="Toahoma 10",

                                command=self.contentLenCount, width=10)

        self.spacelabel4.pack(side=LEFT, padx=3)

        self.countText.pack(side=LEFT, padx=3)

        # 长度计算域text10

        self.text10 = Entry(self.frame6, name="text10", width=5)

        self.text10.pack(side=LEFT, expand=1)

        # frame7

        # 自动内容识别

        self.frame7 = Frame(self)

        self.frame7.pack(pady=10)

        self.spacelabel5 = Label(self.frame7, width=10)

        self.autoLab = Label(self.frame7, text="自动生成话单内容:", font="Toahoma 10")

        self.telType = Label(self.frame7, text="话单类型:", font="Toahoma 10")

        self.autoLab.pack(side=LEFT, padx=3)

        self.autoCheck_choose = BooleanVar()

        self.telType_choose = BooleanVar()

        self.autoCheck = Checkbutton(self.frame7, variable=self.autoCheck_choose,
                                     font="Toahoma 10", command=self.decideLocaltime)
        self.autoCheck.pack(side=LEFT, padx=3)
        self.telCheck = Checkbutton(self.frame7, variable=self.telType_choose,
                                    font="Toahoma 10", command=self.decideLocaltime)
        self.telType.pack(side=LEFT, padx=3)
        self.telCheck.pack(side=LEFT, padx=3)
        self.spacelabel5.pack(side=LEFT, padx=5)
        self.items = (i for i in range(10))
        self.autoLab = Label(self.frame7, text="自动生成内容基础条数:", font="Toahoma 10")
        self.autoLab.pack(side=LEFT, padx=3)
        self.dropdown = Pmw.ComboBox(self.frame7,
                                     #	        labelpos = 'nw',
                                     #          selectioncommand = self.changeColour,
                                     scrolledlist_items=self.items,
                                     entry_width=7
                                     )

        self.dropdown.pack(side=LEFT, padx=5)

        self.spacelabel5.pack(side=LEFT, padx=5)

        self.autoButton = Button(self.frame7, text="生成", font="Toahoma 10",

                                 command=self.submitButton)

        self.autoButton.bind("<Enter>", self.rolloverEnter)  # 鼠标事件:进入

        self.autoButton.bind("<Leave>", self.rolloverLeave)  # 鼠标事件：离开

        self.autoButton.pack(side=LEFT, padx=3)

        # frame9

        self.frame9 = Frame(self)

        self.frame9.pack(pady=10)

        self.messageBar = Pmw.MessageBar(self.frame9,

                                         entry_width=40,

                                         entry_relief='groove',

                                         labelpos='w',

                                         label_text='Status:')

        self.messageBar.pack(fill='x', expand=1, padx=10, pady=5)

        # frame8

        # 版权信息

        self.frame8 = Frame(self)

        self.frame8.pack(pady=10)

        self.versionLab = Label(self.frame8, text="Copyright @2008 SiFang TestWork SoftWare Co..Ltd.", font="Toahoma 9")

        self.versionLab.pack(side=LEFT, padx=3)

    # 文件名计数方法Functon addCount

    def addCount(self):

        self.File_Count += 1

        # 获取即时时间

        data1 = ""

        nowtime = time.localtime()

        for i in range(3):
            # 如果日期为单数需要补零

            data1 += "%02d" % nowtime[i]

        self.text1.delete('-1', 'end')

        self.text1.insert(INSERT,
                          "prm%s_01011%s%s" % (data1, str("%06d" % (self.File_Count)), self.Init_FileCount_Postfix))

    # 文件开始数计数方法Funcation submitButton

    def submitButton(self):

        self.File_Count += 1

        self.text3.delete('-1', 'end')

        self.text3.insert(INSERT, self.File_Count)

        # 获取即时时间

        data1 = ""

        nowtime = time.localtime()

        for i in range(3):
            # 如果日期为单数需要补零

            data1 += "%02d" % nowtime[i]

        self.text1.delete('-1', 'end')

        self.text1.insert(INSERT,
                          "prm%s_01011%s%s" % (data1, str("%06d" % (self.File_Count)), self.Init_FileCount_Postfix))

        # 获取生成文件名、文件记录数、开始文件数、生成文件数、话单间隔时间、主叫号码、被叫号码、主叫步长、被叫步长

        self.FileName = self.text1.get()

        self.FileRecord = int(self.text2.get())

        self.StartCount = int(self.text3.get())

        self.BuildFiles = self.text4.get()

        self.FileSleep = int(self.text5.get())

        self.OrgAddr = int(self.text6.get())

        self.DestAddr = int(self.text8.get())

        self.OrgAddr_add = int(self.text7.get())

        self.DestAddr_add = int(self.text9.get())

        self.Content_tel = str((u'%s' % (self.historyText.get()[:-1])).encode('gbk'))

        #        print u'%s' % (str(self.historyText.get()[:-1]))

        #        print str(self.Content_tel.encode('gbk'))

        self.data1 = data1

        self.decideLocaltime()  # 本地时间，1为启用本地时间，0为获取手工时间

        # 打印生成文件名、文件记录数、开始文件数、生成文件数、话单间隔时间、主叫号码、被叫号码、主叫步长、被叫步长

        #        print self.FileName+"/n"

        #        print self.FileRecord+"/n"

        #        print self.BuildFiles+"/n"

        #        print self.FileSleep+"/n"

        #        print self.OrgAddr+"/n"

        #        print self.DestAddr+"/n"

        #        print self.OrgAddr_add+"/n"

        #        print self.DestAddr_add+"/n"

        # 控制主叫号码

        self.text6.delete('-1', 'end')

        self.text6.insert(INSERT, self.OrgAddr_add + self.OrgAddr)

        # 控制被叫号码

        self.text8.delete('-1', 'end')

        self.text8.insert(INSERT, self.DestAddr_add + self.DestAddr)

        # 调用本地时间判断

        # self.timeControl(self.decideLocaltime())

        # 调用话单文件生成方法

        self.fileExecute(self.timeControl(self.decideLocaltime()))

    # 内容长度计算方法Funcation contentLenCount

    def contentLenCount(self):

        self.contentLenCount = len(str((u'%s' % (self.historyText.get()[:-1])).encode('gbk')))

        self.text10.delete('-1', 'end')

        self.text10.insert(INSERT, self.contentLenCount)

    def fileExecute(self, instead_nowtime):

        # 文件替换的时间

        data1 = instead_nowtime[0]

        # 话单文件中的替换时间

        instead_nowtime = instead_nowtime[1]

        time1, time2 = 0, 0

        for y in range(int(self.BuildFiles)):

            # 循环次数->生成文件数->y

            time1 = time.time()

            global number_OrgAddr, number_DestAddr, count

            count += 1

            newpath = "%s//PTP%s004800%s.txt" % (self.File_Path, self.data1, str("%04d" % (int(self.StartCount + y))))

            list = open(newpath, 'w')

            for i in range(self.FileRecord):

                count += 1

                #                number_OrgAddr += self.OrgAddr_add

                #                number_DestAddr += self.DestAddr_add

                if count == 1:
                    print
                    "dd"

            list.close()

            time.sleep(int(self.FileSleep) / 1000)

            time2 = time.time()

            #            s = u'我是'

            #            print s.encode('gbk')

            s1 = u'生成文件 %s , 当前话单文件包含数据 %s 条 , 每生成一个话单文件所需要的时间：%s 秒' % (
                str("%04d" % (int(self.BuildFiles))), str(self.FileRecord), str(time2 - time1))

            s2 = u'文件生成完毕共计数据%s 条' % (self.FileRecord * self.BuildFiles)

            print
            s1.encode('gbk') + "/n" + s2.encode('gbk')

    def ExitButton(self):

        sys.exit(0)

    def rolloverEnter(self, event):

        event.widget.config(relief=GROOVE)

    def rolloverLeave(self, event):

        event.widget.config(relief=RAISED)

    def changeFont(self):

        desired_font = "Arial 10"

        if self.boldOn.get():
            desired_font += " bold"

        if self.italicOn.get():
            desired_font += " italic"

        print
        desired_font

        self.text5.config(font=desired_font)

    def decideLocaltime(self):

        local_time = 0

        if self.chooseTime.get():
            local_time += 1

        return local_time

    def timeControl(self, choosetime):

        # 是否使用本地时间或者获得手动设置时间

        self.choosetime = choosetime

        # 初始化参数

        data1 = ""

        data2 = ""

        time1 = ""

        if int(self.choosetime) == 0:

            # 使用手工设置时间

            instead_nowtime = self._date.get() + " " + self._time.get()

            data2 = self._date.get()

        else:

            # 使用本地时间

            nowtime = time.localtime()

            for i in range(3):
                # 如果日期为单数需要补零

                data1 += "%02d" % nowtime[i] + "/"

                data2 += "%02d" % nowtime[i]

            for i in range(3, 6):
                # 如果获得日期是单数，则需要补位0

                time1 += "%02d" % nowtime[i] + ':'

                # time1 += "%02d" % nowtime[i]

            instead_nowtime = data2 + " " + time1

        return data1, instead_nowtime

    def showContents(self, event):

        the_name = event.widget.winfo_name()

        the_contents = event.widget.get()

        showinfo("Message", the_name + ":" + the_contents)


def main():
    import tkinter

    root = tkinter.Tk()

    Pmw.initialise(root)

    widget = GUIFrame(root)

    root.mainloop()


if __name__ == "__main__":
    main()
