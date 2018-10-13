#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
wx.EvtHandler类定义的一些方法在一般情况下用不到。你会经常使用的
wx.EvtHandler的方法是Bind(),它创建事件绑定。该方法的用法如下:
Bind(event, handler, source=None, id=wx.ID_ANY, id2=wx.ID_ANY)
Bind()函数将一个事件和一个对象与一个事件处理器函数关联起来。参数
event是必选的,它是我们在3.3节中所说的wx.PyEventBinder的一个实例。参数
handler也是必选的,它是一个可调用的Python对象,通常是一个被绑定的方法
或函数。处理器必须是可使用一个参数(事件对象本身)来调用的。参数
handler可以是None,这种情况下,事件没有关联的处理器。参数source是产生
该事件的源窗口部件,这个参数在触发事件的窗口部件与用作事件处理器的窗
口部件不相同时使用。通常情况下这个参数使用默认值None,这是因为你一般
使用一个定制的wx.Frame类作为处理器,并且绑定来自于包含在该框架内的窗
口部件的事件。父窗口的__init__是一个用于声明事件绑定的方便的位置。但是
如果父窗口包含了多个按钮敲击事件源(比如OK按钮和Cancel按钮),那么就
要指定source参数以便wxPython区分它们。下面是该方法的一个例子:
self.Bind(wx.EVT_BUTTON, self.OnClick, button)

常用eventHandler方法
AddPendingEvent(event):将这个event参数放入事件处理系统中。类似于
ProcessEvent(),但它实际上不会立即触发事件的处理。相反,该事件被增加到事件
队列中。适用于线程间的基于事件的通信。
Bind(event, handler, source=None,   id=wx.ID_ANY, id2=wx.ID_ANY):完整的说明
见3.3.1节。
GetEvtHandlerEnabled()
SetEvtHandlerEnabled( boolean):如果处理器当前正在处理事件,则属性为True,
否则为False。
ProcessEvent(event):把event对象放入事件处理系统中以便立即处理。
"""

__author__ = 'tomtiddler'

import wx

"""
class DoubleEventFrame(wx.Frame):

    def __init__(self, parent, id):
        super(DoubleEventFrame, self).__init__(parent, id, 'Frame With Button', size=(300, 100))
        self.panel = wx.Panel(self, -1)
        self.button = wx.Button(self.panel, -1, "Click Me", pos=(100, 15))
        # 1 这行绑定框架关闭事件到self.OnCloseWindow方法。由于这个事件通过
        # 该框架触发且用于帧, 所以不需要传递一个source参数。
        self.Bind(wx.EVT_CLOSE, self.on_close_window)

        # 2 这行将来自按钮对象的按钮敲击事件绑定到self.OnCloseMe方法。这样
        # 做是为了让wxPython能够区分在这个框架中该按钮和其它按钮所产生的事件。
        self.Bind(wx.EVT_BUTTON, self.on_button_click,
                  self.button)  # 2 绑定按钮敲击事件

    def on_close_window(self, event):
        self.Close(True)

    def on_button_click(self, event):
        self.Destroy()
"""


class MenuEventFrame(wx.Frame):
    """
    你也可以使用source参数来标识项目, 即使该项目不是事件的源。例如,
    你可以绑定一个菜单事件到事件处理器, 即使这个菜单事件严格地说是由框架
    所触发的。
    以下演示了绑定一个菜单事件的例子:
    """
    def __init__(self, parent, id):
        super(MenuEventFrame, self).__init__(parent, id, "Menus", size=(300, 200))
        menu_bar = wx.MenuBar()
        menu1 = wx.Menu()
        menu_item = menu1.Append(-1, "Exit...")
        menu_bar.Append(menu1, "File")
        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.on_close_me, menu_item)

    def on_close_me(self, event):
        self.Close(True)


if __name__ == "__main__":
    app = wx.App()
    frame = MenuEventFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()



















"""
class ButtonEventFrame(wx.Frame):

    def __init__(self, parent, id):
        super(ButtonEventFrame, self).__init__(parent, id, 'Frame With Button', size=(300, 100))
        self.panel = wx.Panel(self, -1)
        self.button = wx.Button(self.panel, -1, "Click Me", pos=(100, 15))
        self.button2 = wx.Button(self.panel, -1, "Click You", pos=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.on_button_click, self.button)  # 1 绑定按钮敲击事件
        self.Bind(wx.EVT_BUTTON, self.on_button_click2, self.button2)

    def on_button_click(self, event):
        self.panel.SetBackgroundColour('Green')
        self.panel.Refresh()

    def on_button_click2(self, event):
        self.panel.SetBackgroundColour('White')
        self.panel.Refresh()


if __name__ == "__main__":
    app = wx.App()
    frame = ButtonEventFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
"""