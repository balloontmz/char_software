#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

import wx


class RefactorExample(wx.Frame):
    def __init__(self, parent, id):
        super(RefactorExample, self).__init__(parent, id, 'Refactor Example', size=(340, 200))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour("White")
        self.Bind(wx.EVT_CLOSE, self.on_close_window)
        self.create_menu_bar()

        self.create_button_bar(panel)
        self.create_text_fields(panel)

    def menu_datas(self):
        return (
            ("file", (
                ("open", "open on status bar", self.on_open),
                ("quit", "quit", self.on_close_window)
            )),
            ("edit", (
                ("copy", "copy", self.on_copy),
                ("cut", "cut", self.on_cut),
                ("paste", "paste", self.on_paste),
                ("", "", ""),
                ("options", "displayOptions", self.on_options)
            ))
        )

    def create_menu_bar(self):
        menu_bar = wx.MenuBar()
        for each_menu_data in self.menu_datas():
            menu_label = each_menu_data[0]
            menu_items = each_menu_data[1]
            menu_bar.Append(self.create_menu(menu_items), menu_label)
        self.SetMenuBar(menu_bar)

    def create_menu(self, menu_data):
        menu = wx.Menu()
        for label, status, handler in menu_data:
            if not label:
                menu.AppendSeparator()  # 此方法的作用 从效果来看，生成了一个分割线
                continue
            menu_item = menu.Append(-1, label, status)
            self.Bind(wx.EVT_MENU, handler, menu_item)
        return menu

    def text_fields_data(self):
        return (
            ("First name", (10, 50)),
            ("Last name", (10, 80))
        )

    def create_text_fields(self, panel):
        for label, pos in self.text_fields_data():
            self.create_caption_text(panel, label, pos)

    def create_caption_text(self, panel, label, pos):
        static = wx.StaticText(panel, wx.NewIdRef(), label, pos)
        static.SetBackgroundColour("White")
        text_pos = (pos[0] + 80, pos[1])
        wx.TextCtrl(panel, wx.NewIdRef(), size=(100, -1), pos=text_pos)

    def button_data(self):
        return(
            ("FIRST", self.on_first),
            ("<<PREV", self.on_prev),
            ("NEXT>>", self.on_next),
            ("LAST", self.on_last),
        )

    def create_button_bar(self, panel, y_pos=0):
        x_pos = 0
        for label, handler in self.button_data():
            pos = (x_pos, y_pos)
            button = self.build_one_button(panel, label, handler, pos)
            x_pos += button.GetSize().width

    def build_one_button(self, parent, label, handler, pos=(0, 0)):
        button = wx.Button(parent, -1, label, pos)
        self.Bind(wx.EVT_BUTTON, handler, button)
        return button

    # Just grouping the empty event handlers together
    def on_prev(self, event): pass

    def on_next(self, event): pass

    def on_last(self, event): pass

    def on_first(self, event): pass

    def on_open(self, event): pass

    def on_copy(self, event): pass

    def on_cut(self, event): pass

    def on_paste(self, event): pass

    def on_options(self, event): pass

    def on_close_window(self, event):
        self.Destroy()


if __name__ == "__main__":
    app = wx.App()
    frame = RefactorExample(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
