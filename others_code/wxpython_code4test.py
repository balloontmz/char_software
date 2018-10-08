#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://blog.csdn.net/a_lazy_zhu/article/details/80159769
Wxpython 事件的定义与绑定
    1.定义事件函数
        事件函数不能接受其它参数，只能接受 event 的参数
    2.将事件函数和我们组件触发的事件绑定起来
"""

__author__ = 'tomtiddler'

import wx


# 定义事件函数
# 读函数
def open_file(event):
    """
    getvalue 是获取文本框的值
    setvalue 是设置文本框的值
    """
    with open(pathText.GetValue(), "r") as f:
        content.SetValue(f.read())
    # 写函数


def save_file(event):
    with open(pathText.GetValue(), "w") as f:
        f.write(content.GetValue())


app = wx.App()
frame = wx.Frame(None, title="MyFrame", size=(420, 350))
panel = wx.Panel(frame)  # 创建画布，以主窗口为父
but1 = wx.Button(panel, label="save")  # 以画布为父类
but2 = wx.Button(panel, label="open")

# 绑定事件
but2.Bind(wx.EVT_BUTTON, open_file)
but1.Bind(wx.EVT_BUTTON, save_file)

pathText = wx.TextCtrl(panel)  # 以画布为父类
content = wx.TextCtrl(panel)

# 声明尺寸器
sBox = wx.BoxSizer()  # 水平尺寸器，不带参数则为默认的水平尺寸器
vBox = wx.BoxSizer(wx.VERTICAL)  # 垂直尺寸器

# 给尺寸器添加组件，从左往右，从上到下
sBox.Add(pathText, proportion=3, flag=wx.EXPAND | wx.ALL, border=5)
sBox.Add(but1, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
sBox.Add(but2, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

vBox.Add(sBox, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
vBox.Add(content, proportion=5, flag=wx.EXPAND | wx.ALL, border=5)

# 设置主尺寸
panel.SetSizer(vBox)  # 因为sBox被嵌套在vBox上，所以以vBox为主尺寸

frame.Show()  # 因为文本组件和按钮组件都是以窗框组件为父组件，所以只需要调用frame

if __name__ == "__main__":
    app.MainLoop()
