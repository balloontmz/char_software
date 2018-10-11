#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
linux的菜单栏在顶部
菜单栏、工具栏、状态栏  由框架进行管理，而不是画布
"""

__author__ = 'tomtiddler'

import wx
import wx.py.images as images


class ToolBarFrame(wx.Frame):
    def __init__(self, parent, nid):
        super(ToolBarFrame, self).__init__(parent, id=nid, title="ToolBars", size=(300, 200))
        panel = wx.Panel(self)
        panel.SetBackgroundColour("White")
        # 1 创建状态栏  出现了状态栏--虽然没有显式调用 这行创建了一个状态栏,它是类wx.StatusBar的实例。它被放置在框架
        # 的底部,宽度与框架相同,高度由操作系统决定。状态栏的目的是显示在应用
        # 程序中被各种事件所设置的文本。
        status_bars = self.CreateStatusBar()

        # 2 创建工具栏创建了一个wx.ToolBar的实例, 它是命令按钮的容器。它被自动放置在框架的顶部
        toolbar = self.CreateToolBar()
        # 3 给工具栏增加一个工具
        toolbar.AddTool(wx.NewIdRef(), "NEW",
                        images.getPyBitmap(), wx.NullBitmap, shortHelp="new", longHelp="Long Help for new")
        toolbar.Realize()  # 4 准备显示工具栏

        # 创建菜单的项目, 其中参数分别代表ID, 选项的文本, 当鼠标位于其上时显示在状态栏的文本。
        menu_bar = wx.MenuBar()  # 创建菜单栏
        # 创建两个菜单
        menu1 = wx.Menu()
        menu_bar.Append(menu1, "File")

        menu2 = wx.Menu()
        menu2.Append(wx.NewIdRef(), "COPY", "Copy in status bar")
        menu2.Append(wx.NewIdRef(), "Cut", "")
        menu2.Append(wx.NewIdRef(), "Paste", "")
        menu2.AppendSeparator()
        menu2.Append(wx.NewIdRef(), "Options...", "Display Options")
        menu_bar.Append(menu2, "Edit")  # 在菜单栏上附上菜单
        self.SetMenuBar(menu_bar)  # 在框架上附上菜单栏


if __name__ == "__main__":
    app = wx.App()
    frame = ToolBarFrame(None, -1)
    frame.Show()
    app.MainLoop()

