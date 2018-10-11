#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

import wx


class ClientGui(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None,
                               title="Chat Room")
        self.frame.SetDimensions(-1, -1, 500, 500)
        self.frame.Show()
        return True


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)
        self.panel = MainPanel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize()


class MainPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(MainPanel, self).__init__(*args, **kwargs)

        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        left_sizer = wx.BoxSizer(wx.VERTICAL)
        right_sizer = wx.BoxSizer(wx.VERTICAL)

        # LeftPanel: TextDisplay, TextInput, SendButton
        style = style = wx.TE_MULTILINE | wx.TE_RICH2
        self.textDisplay = wx.TextCtrl(self, style=style)
        self.textInput = wx.TextCtrl(self, style=style)
        self.sendBtn = wx.Button(self, label="Send")
        ##
        left_sizer.Add(self.textDisplay, 1, wx.EXPAND | wx.ALL, 5)
        left_sizer.Add(self.textInput, 1, wx.EXPAND | wx.ALL, 5)
        left_sizer.Add(self.sendBtn, 0, wx.ALIGN_CENTER_HORIZONTAL)

        # RightPanel: NumLabel, UserList, QuitButton
        self.onlineNum = wx.StaticText(self, label="chat online")
        self.userList = wx.ListCtrl(self)
        self.quitBtn = wx.Button(self, label="Quit")
        ##
        right_sizer.Add(self.onlineNum, 0, wx.ALIGN_CENTER_HORIZONTAL)
        right_sizer.Add(self.userList, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND | wx.ALL, 5)
        right_sizer.Add(self.quitBtn, 0, wx.ALIGN_CENTER_HORIZONTAL)

        hsizer.Add(left_sizer, 2, wx.EXPAND)
        hsizer.Add(right_sizer, 1, wx.EXPAND)

        self.SetSizer(hsizer)


if __name__ == '__main__':
    app = ClientGui(False)
    app.MainLoop()
