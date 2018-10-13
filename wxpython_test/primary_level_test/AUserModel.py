#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
一个简单的自定义的MVC模型
"""

__author__ = 'tomtiddler'

import wx


class AbstractModel(object):
    """
    一个抽象的基类
    """

    def __init__(self):
        self.listeners = []

    def add_listener(self, listener_func):
        self.listeners.append(listener_func)

    def remove_listener(self, listener_func):
        self.listeners.remove(listener_func)

    def update(self):
        for eachFunc in self.listeners:
            eachFunc(self)


class SimpleName(AbstractModel):
    """基于基类的model"""

    def __init__(self, first="", last=""):
        super(SimpleName, self).__init__()
        self.set(first, last)
        self.first = None
        self.last = None

    def set(self, first, last):
        self.first = first
        self.last = last
        self.update()  # 1 更新


class ModelExample(wx.Frame):
    """view 和 controler 两个功能"""

    def __init__(self, parent, id):
        super(ModelExample, self).__init__(parent, id, 'Flintstones', size=(340, 200))
        panel = wx.Panel(self)
        panel.SetBackgroundColour("White")
        self.Bind(wx.EVT_CLOSE, self.on_close_window)
        self.textFields = {}
        self.create_text_fields(panel)
        # -------------------------------
        # 2 创建模型
        self.model = SimpleName()
        self.model.add_listener(self.on_update)
        # -------------------------------
        self.create_button_bar(panel)

    def button_data(self):
        return (("Fredify", self.on_fred),
                ("Wilmafy", self.on_wilma),
                ("Barnify", self.on_barney),
                ("Bettify", self.on_betty))

    def create_button_bar(self, panel, yPos=0):
        xPos = 0
        for eachLabel, eachHandler in self.button_data():
            pos = (xPos, yPos)
            button = self.build_one_button(panel, eachLabel, eachHandler, pos)
            xPos += button.GetSize().width

    def build_one_button(self, parent, label, handler, pos=(0, 0)):
        button = wx.Button(parent, -1, label, pos)
        self.Bind(wx.EVT_BUTTON, handler, button)
        return button

    def text_field_data(self):
        return (("First Name", (10, 50)),
                ("Last Name", (10, 80)))

    def create_text_fields(self, panel):
        for eachLabel, eachPos in self.text_field_data():
            self.create_captioned_text(panel, eachLabel, eachPos)

    def create_captioned_text(self, panel, label, pos):
        static = wx.StaticText(panel, wx.NewIdRef(), label, pos)
        static.SetBackgroundColour("White")
        textPos = (pos[0] + 75, pos[1])
        # 将动态文本对象赋值给字典的value，然后对其更新可转换为对该value的更新
        self.textFields[label] = wx.TextCtrl(panel, wx.NewIdRef(),
                                             "", size=(100, -1), pos=textPos,
                                             style=wx.TE_READONLY)

    def on_update(self, model):  # 3 设置文本域
        self.textFields["First Name"].SetValue(model.first)
        self.textFields["Last Name"].SetValue(model.last)

    # -------------------------------------------

    # 4 响应按钮敲击的处理器
    def on_fred(self, event):
        self.model.set("Fred", "Flintstone")

    def on_barney(self, event):
        self.model.set("Barney", "Rubble")

    def on_wilma(self, event):
        self.model.set("Wilma", "Flintstone")

    def on_betty(self, event):
        self.model.set("Betty", "Rubble")

    # ---------------------------------------------   
    def on_close_window(self, event):
        self.Destroy()


if __name__ == "__main__":
    app = wx.App()
    frame = ModelExample(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
