#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

import wx


class MouseEventFrame(wx.Frame):
    """
    一个事件是否向上展开至容器级,这是每个事件实例的一个动态属性,尽
管实际上默认值几乎总是使用那几个。默认情况,只有wx.CommandEvent及其
子类的实例向上展开至容器级。其它的所有事件不这样做。
    在下例中,按钮敲击事件得到处理。在wx.Button上敲击鼠标产生一个命
令类型的事件wx.EVT_BUTTON。由于wx.EVT_BUTTON属于一个
wx.CommandEvent,所以wxPython在这个按钮对象中找寻绑定失败后,它将向
上展开至容器级,先是按钮的父窗口panel。由于panel中没有相匹配的绑定,所
以又向上至panel的父窗口frame。由于frame中有匹配的绑定,所以
ProcessEvent()调用相关函数 OnButtonClick()。
    同时也说明了为什么鼠标进入和离开事件必须被绑定到按钮而不是
框架。由于鼠标事件不是wx.CommandEvent的子类,所以鼠标进入和离开事件
不向上展开至容器级。如果鼠标进入和离开事件被绑定到了框架,那么当鼠标
进入或离开框架时,wxPython触发鼠标进入或离开事件。
    在这种方式中,命令事件是被优先对待的。因为它们被认为是高级事件,
表示用户正在应用程序空间中做一些事,而非窗口系统。窗口系统类型事件只
对窗口部件感兴趣,而应用级事件对容器级。这个规则不防碍我们在任何地方
声明绑定,不管被绑定的是什么对象或什么对象定义事件处理器。例如,即使
这个绑定的鼠标敲击事件针对于按钮对象,而绑定则被定义在这个框架类中,
且调用这个框架内的方法。换句话说,低级的非命令事件通常用于窗口部件或
一些系统级的通知,如鼠标敲击、按键按下、绘画请求、调整大小或移动。另
一方面,命令事件,如在按钮上敲击鼠标、或列表框上的选择,通常由窗口部
件自己生成。例如,在适当的窗口部件上按下和释放鼠标后,按钮命令事件产
生。
    最后,如果遍历了容器级后,事件没有被处理,那么应用程序的wx.App对
象调用ProcessEvent()。默认情况下,这什么也不做,但是你可以给你的wx.App
增加事件绑定,以便以非标准的方式来传递事件。例如,假如你在写一个GUI
构建器,你可能想把你构建器窗口中的事件传到你的代码窗口中,即使它们都
是顶级窗口。方法之一是捕获应用程序对象中的事件,并把它们传递到代码窗
口上。
    """
    def __init__(self, parent, id):
        super(MouseEventFrame, self).__init__(parent, id, "Frame With Button", size=(300, 100))
        self.panel = wx.Panel(self)
        self.button = wx.Button(self.panel, label="Not Over", pos=(100, 15))
        # 按钮上发生的事件，没找到对应的处理器函数，向上展开到frame查找相应的方法。该事件绑定到了source参数上
        self.Bind(wx.EVT_BUTTON, self.on_button_click, self.button)
        self.button.Bind(wx.EVT_ENTER_WINDOW, self.on_enter_window)
        self.button.Bind(wx.EVT_LEAVE_WINDOW, self.on_leave_window)

    def on_button_click(self, event):
        self.panel.SetBackgroundColour("Green")

    def on_enter_window(self, event):
        self.button.SetLabel("Over Me")

    def on_leave_window(self, event):
        self.button.SetLabel("Leave Me")


if __name__ == "__main__":
    app = wx.App()
    frame = MouseEventFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()


