#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
bare.py
显示一个图像的窗口
这个基本的wxPython程序说明了开发任一wxpython程序所必须的五个基本步骤：
1. 导入必须的wxpython包
2. 子类化wxpython应用程序类
3. 定义一个应用程序的初始化方法
4. 创建一个应用程序的实例
5. 进入这个应用程序的主事件循环

对于导入顺序需要注意的是:你从wxPython导入其它东西之前必须先导入
wx。通常情况下,Python中的模块导入顺序无关。但是wxPython中的不同,它
是一个复杂的模块。当你第一次导入wx模块时,wxPython要对别的wxPython模
块执行一些初始化工作。例如wxPython中的一些子包,如xrc模块,它在wx模
块导入之前不能够正确的工作,我们必须按下面顺序导入:
import wx
from wx import xrc

一旦你导入了wx模块,你就能够创建你的应用程序(application)对象和
框架(frame)对象。每个wxPython程序必须有一个application对象和至少一个
frame对象。application对象必须是wx.App的一个实例或你在OnInit()方法中定义
的一个子类的一个实例。当你的应用程序启动的时候,OnInit()方法将被
wx.App父类调用。

一旦进入主事件循环,控制权将转交给wxPython。wxPython GUI程序主要
响应用户的鼠标和键盘事件。当一个应用程序的所有框架被关闭后,这个
app.MainLoop()方法将返回且程序退出。
"""

__author__ = 'tomtiddler'

import wx  # 1


class App(wx.App):  # 2

    def OnInit(self):  # 3
        frame = wx.Frame(parent=None, title="Bare")
        frame.Show()
        # frame.Show(False)  # 使框架不可见.
        # frame.Show(True)  # True是默认值,使框架可见.
        # frame.Hide()  # 等同于frame.Show(False)
        return True


if __name__ == "__main__":
    app = App()  # 4
    app.MainLoop()  # 5
