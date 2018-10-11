#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
创建一个有一个文本框的窗口用来显示鼠标的位置
"""

__author__ = 'tomtiddler'

import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super(MyFrame, self).__init__(None, -1, "My Frame", size=(300, 300))  # 主窗口
        # wx.Frame.__init__(self, None, -1, "My Frame", size=(300, 300))
        panel = wx.Panel(self, -1)  # 画布
        panel.Bind(wx.EVT_MOTION, self.OnMove)  # wx.EVT_MOTION 事件  OnMove 事件处理器
        wx.StaticText(panel, -1, "POS:", pos=(40, 10))  # 静态文本
        self.postCtrl = wx.TextCtrl(panel, -1, "", pos=(40, 10))  # 动态文本

    def OnMove(self, event):
        pos = event.GetPosition()
        self.postCtrl.SetValue("%s, %s" % (pos.x, pos.y))


if __name__ == "__main__":
    app = wx.PySimpleApp()  # 应用程序类
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()
