#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    wx.grid.PyGridTableBase的必须的方法
GetNumberRows():返回一个表明grid中行数的整数。
GetNumberCols():返回一个表明grid中列数的整数。
IsEmptyCell(row, col):如果索引(row,col)所表示的单元是空的话,返回True。
GetValue(row, col):返回显示在单元(row,col)中的值。
SetValue(row, col,value):设置单元(row,col)中的值。如果你想要只读模式,你仍必
须包含这个方法,但是你可以在该函数中使用pass。
"""

__author__ = 'tomtiddler'

import wx
import wx.grid


class LineupTable(wx.grid.GridTableBase):
    data = (("CF", "Bob", "Dernier"),
            ("2B", "Ryne", "Sandberg"),
            ("LF", "Gary", "Matthews"),
            ("1B", "Leon", "Durham"),
            ("RF", "Keith", "Moreland"),
            ("3B", "Ron", "Cey"),
            ("C", "Jody", "Davis"),
            ("SS", "Larry", "Bowa"),
            ("P", "Rick", "Sutcliffe")
            )

    clo_labels = ("Last", "First")

    def __init__(self):
        super(LineupTable, self).__init__()

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data[0]) - 1

    def GetColLabelValue(self, col):
        return self.clo_labels[col]

    def GetRowLabelValue(self, row):
        return self.data[row][0]

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        return self.data[row][col + 1]

    def SetValue(self, row, col, value):
        pass


class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent):
        super(SimpleGrid, self).__init__(parent, -1)
        self.SetTable(LineupTable())


class TestFrame(wx.Frame):
    def __init__(self, parent):
        super(TestFrame, self).__init__(parent, -1, "A Grid", size=(275, 275))
        grid = SimpleGrid(self)


if __name__ == "__main__":
    app = wx.App()
    frame = TestFrame(None)
    frame.Show(True)
    app.MainLoop()

