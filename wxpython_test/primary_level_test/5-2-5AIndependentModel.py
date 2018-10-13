#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
抽象的一个独立的模型，该模型对一个单独的行进行操作。没有实际运行，由于GridTableBase的内存bug，暂时该类不知如何使用。
"""

__author__ = 'tomtiddler'

import wx
import wx.grid


class LineupEntry:
    def __init__(self, pos, first, last):
        self.pos = pos
        self.first = first
        self.last = last


class LineupTable(wx.grid.PyGridTableBase):
    colLabels = ("First", "Last")  # 列标签

    colAttrs = ("first", "last")  # 1 属性名

    def __init__(self, entries):  # 2 初始化模型
        wx.grid.PyGridTableBase.__init__(self)
        self.entries = entries

    def GetNumberRows(self):
        return len(self.entries)

    def GetNumberCols(self):
        return 2

    def GetColLabelValue(self, col):
        return self.colLabels[col]  # 读列标签

    def GetRowLabelValue(self, col):
        return self.entries[row].pos  # 3 读行标签

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        entry = self.entries[row]
        return getattr(entry, self.colAttrs[col])  # 4 读属性值

    def SetValue(self, row, col, value):
        pass


if __name__ == "__main__":
    pass
