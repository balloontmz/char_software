#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
spare

"""

__author__ = 'tomtiddler'

import wx


class App(wx.App):
    def __init__(self):
        super(App, self).__init__()
        self.frame = None

    def OnInit(self):
        # 我们将对frame实例的引用作为应用程序实例的一个属性
        self.frame = Frame(parent=None, title='Spare')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


class Frame(wx.Frame):
    pass


if __name__ == "__main__":
    app = App()
    app.MainLoop()
