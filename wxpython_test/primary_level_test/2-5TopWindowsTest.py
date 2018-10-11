#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

import wx


if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None, id=wx.NewIdRef(), pos=(500, 300), size=(200, 200),
                     style=wx.DEFAULT_FRAME_STYLE)
    iid = frame.GetId()
    print(iid)
    frame.Show()
    app.MainLoop()

