#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

import wx
import wx.grid


class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent):
        super(SimpleGrid, self).__init__(parent, -1)
        self.CreateGrid(9, 2)
        self.SetColLabelValue(0, "First")
        self.SetColLabelValue(1, "Last")
        self.SetRowLabelValue(0, "CF")
        self.SetCellValue(0, 0, "bob")
        self.SetCellValue(0, 1, "Dernier")


class TestFrame(wx.Frame):
    def __init__(self, parent):
        super(TestFrame, self).__init__(parent, -1, "A Grid", size=(275, 275))
        grid = SimpleGrid(self)


if __name__ == "__main__":
    app = wx.App()
    frame = TestFrame(None)
    frame.Show(True)
    app.MainLoop()


