#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

import wx


if __name__ == "__main__":
    app = wx.App()
    # 选择对话框，返回值保存在result里面 返回值为以下常量wx.ID_YES, wx.ID_NO, wx.ID_CANCEL, wx.ID_OK
    # dlg = wx.MessageDialog(parent=None,
    #                        message='Is this the coolest thing ever!,’MessageDialog’',  # 以上两个为位置参数
    #                        style=wx.YES_NO | wx.ICON_QUESTION)
    # result = dlg.ShowModal()
    # dlg.Destroy()

    # 文本输入对话框， ShowMoDal返回按钮ID， GetValue得到用户输入
    # dlg = wx.TextEntryDialog(None, "Who is buried in Grant’s tomb?”,’A Question’, ’Cary Grant")
    # if dlg.ShowModal() == wx.ID_OK:
    #     response = dlg.GetValue()
    #     print(response)
    # dlg.Destroy()

    # wx.SingleChoiceDialog的参数类似于文本输入对话框, 只是以字符串的列
    # 表代替了默认的字符串文本。要得到所选择的结果有两种方法, GetSelection()
    # 方法返回用户选项的索引, 而GetStringSelection()
    # 返回实际所选的字符串。
    dlg = wx.SingleChoiceDialog(None, "What version of python are you using",
                                'Single CHOICE',  # 标签
                                ['1.5', '2.0', '2.5', '3.0'])
    if dlg.ShowModal() == wx.ID_OK:
        response = dlg.GetStringSelection()
        print(response)
    dlg.Destroy()

    # app.MainLoop() 此行注释掉未影响代码运行， 据此，当代码运行结束并且事件全部结束，主事件循环也就结束了。


