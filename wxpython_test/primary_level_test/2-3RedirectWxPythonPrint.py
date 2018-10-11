#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
所有的Python程序都能够通过两种标准流来输出文本:分别是标准输出流
sys.stdout和标准错误流sys.stderr。通常,Python脚本定向标准输出流到它所运
行的控制台。然而,当你的应用程序对象被创建时,你可以决定使用wxPython
控制标准流并重定向输出到一个窗口。在Windows下,这个重定向行为是
wxPython的默认行为。而在Unix系统中,默认情况下,wxPython不控制这个标
准流。在所有的系统中,当应用程序对象被创建的时候,重定向行为可以被明
确地指定。我们推荐利用这个特性并总是指定重定向行为来避免不同平台上的
不同行为产生的任何问题。

下例同时演示了应用程序的生命周期和重定向输出
通过输出演示周期
"""

__author__ = 'tomtiddler'

import sys

import wx


class App(wx.App):
    def __init__(self, redirect=True, filename=None):
        print("APP init")  # 此时应用程序未完成初始化，该输出依旧为控制台输出
        self.frame = None
        super(App, self).__init__(redirect=redirect, filename=filename)

    def OnInit(self):
        print("OnInit")
        self.frame = Frame(parent=None, id=-1, title="StartUp")
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print("A pretend err message")
        return True

    def OnExit(self):
        print("OnExit")  # 此行重定向成功，但是由于窗口关闭太快，没来得及显示，或许可以加定时器


class Frame(wx.Frame):
    def __init__(self, parent, id, title):
        print("Frame init")
        super(Frame, self).__init__(parent=parent, id=id, title=title)


if __name__ == "__main__":
    # 1 文本定向从这里开始,包括stdout和stderr两种，同时，还能跟一个filename参数指定输出到文件
    # app = App(redirect=False)
    # app = App(True, "2-3output")
    app = App(redirect=True)
    print("before MainLoop")
    app.MainLoop()  # 2 进入主事件循环
    print("after MainLoop")

