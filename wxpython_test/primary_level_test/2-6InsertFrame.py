#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

import wx


class App(wx.App):
    pass


class InsertFrame(wx.Frame):
    def __init__(self, parent, id):
        super(InsertFrame, self).__init__(parent, id=id, title="Frame With Button", size=(300, 100))
        panel = wx.Panel(self)  # 创建画板
        button = wx.Button(panel, label="Close", pos=(125, 10), size=(50, 50))  # 将按钮添加到画板
        # 绑定按钮的点击事件
        self.Bind(wx.EVT_BUTTON, self.on_close_me, button)
        # 绑定窗口的关闭事件，此事件是系统自动绑定的。无需自己定义
        # self.Bind(wx.EVT_CLOSE, self.on_close_window)

    def on_close_me(self, event):
        self.Close(True)

    def on_close_window(self, event):
        self.Destroy()


if __name__ == "__main__":
    app = App()
    frame = InsertFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()

