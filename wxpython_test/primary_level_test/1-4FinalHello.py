#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Frame 参数列表
wx.Frame(parent, id=-1, title=””, pos=wx.DefaultPosition,
        size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE,
        name=”frame”)

parent: 框架的父窗口。对于顶级窗口,这个值是None。框架随其父窗口的销毁而
销毁。取决于平台,框架可被限制只出现在父窗口的顶部。在多文档界面的情况下,
子窗口被限制为只能在父窗口中移动和缩放。
id: 关于新窗口的wxPython ID号。你可以明确地传递一个。或传递-1,这将导致
wxPython自动生成一个新的ID。
title:窗口的标题。
pos: 一个wx.Point对象,它指定这个新窗口的左上角在屏幕中的位置。在图形用户
界面程序中,通常(0,0)是显示器的左上角。这个默认的(-1,-1)将让系统决定窗口的位
置。
size: 一个wx.Size对象,它指定这个窗口的初始尺寸。这个默认的(-1,-1)将让系统决
定窗口的初始尺寸。
style: 指定窗口的类型的常量。你可以使用或运算来组合它们。
name: 框架的内在的名字。以后你可以使用它来寻找这个窗口。
"""

__author__ = 'tomtiddler'

import wx


class App(wx.App):  # 定义一个带OnInit方法的app子类，这是wxapp最基本的要求

    def __init__(self):
        super(App, self).__init__()
        self.frame = None

    def OnInit(self):
        # 读取同目录下的jpeg文件创建一个Image对象
        image = wx.Image('wxPython.jpeg', wx.BITMAP_TYPE_JPEG)
        self.frame = Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


class Frame(wx.Frame):  # 2wx.frame子类,以便更加容易控制框架的内容和外观
    """Frame class that displays an image"""

    def __init__(self,
                 image,
                 parent=None,
                 id=-1,
                 pos=wx.DefaultPosition,
                 title='Hello wxpython!'):
        # 3给原始构造器增加一个图像参数，这个值在应用程序类在创建框架实例的时候提供，同时，我们需要初始化原初始化函数
        # 4.采用控件显示图像，该控件要求一个位图，所以我们转换为位图。同时，获取图片的尺寸传递给框架对象，方便框架调用
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        super(Frame, self).__init__(parent=parent, id=id, pos=pos, title=title, size=size)
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)


if __name__ == "__main__":
    app = App()  # 创建一个实例并启动事件循环
    app.MainLoop()
