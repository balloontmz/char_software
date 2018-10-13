#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
这个暂时放到后面吧，暂时应该是理不清的。
"""

__author__ = 'tomtiddler'

import wx


class TwoButtonEvent(wx.PyCommandEvent):  # 定义事件类
    def __init__(self, evt_type, id):
        super(TwoButtonEvent, self).__init__(evt_type, id)
        self.click_count = 0

    def get_click_count(self):
        return self.click_count

    def set_click_count(self, count):
        self.click_count = count


myEVT_TWO_BUTTON = wx.NewEventType()  # 创建一个事件类型
EVT_TWO_BUTTON = wx.PyEventBinder(myEVT_TWO_BUTTON, 1)


class TwoButtonPanel(wx.Panel):
    def __init__(self, parent, id=-1, left_text="Left", right_text="Right"):
        super(TwoButtonPanel, self).__init__(parent, id)
        self.leftButton = wx.Button(self, label=left_text)
        self.rightButton = wx.Button(self, label=right_text, pos=(100, 0))
        self.left_click = False
        self.right_click = False
        self.click_count = 0

        self.leftButton.Bind(wx.EVT_LEFT_DOWN, self.on_left_click)
        self.rightButton.Bind(wx.EVT_LEFT_DOWN, self.on_right_click)

    def on_left_click(self, event):
        self.leftButton = True
        self.on_click()
        event.Skip()

    def on_right_click(self, event):
        self.rightButton = True
        self.on_click()
        event.Skip()

    # 此处为处理新建事件的核心代码
    def on_click(self):
        self.click_count += 1
        if self.leftButton and self.rightButton:
            self.leftButton = False
            self.rightButton = False
            evt = TwoButtonEvent(myEVT_TWO_BUTTON, self.GetId())
            evt.set_click_count(self.click_count)
            self.GetEventHandler().ProcessEvent(evt)


class CustomEventFrame(wx.Frame):
    def __init__(self, parent, id):
        super(CustomEventFrame, self).__init__(parent, id, "Click Count:0", size=(300, 100))
        panel = TwoButtonPanel(self)
        self.Bind(EVT_TWO_BUTTON, self.on_two_click, panel)

    def on_two_click(self, event):
        self.SetTitle("Click Count:%s" % event.get_click_count())


if __name__ == "__main__":
    app = wx.App()
    frame = CustomEventFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()


