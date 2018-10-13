#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
一个单元测试
说明:
    #1:声明unittest.TestCase的一个子类。为了最好的使每个测试相互独立,
测试执行器为每个测试创建该类的一个实例。
    #2: setUp()方法在每个测试被执行前被调用。这使得你能够保证每个对你
的应用程序的测试都处在相同的状态下。这里我们创建了一个用于测试的框架
(frame)的实例。
    #3 :tearDown()方法在每个测试执行完后被调用。这使得你能够做一些清
理工作,以确保从一个测试转到另一个测试时系统状态保持一致。通常这里包
括重置全局数据,关闭数据库连接等诸如此类的东东。这里我们对框架调用了
Destroy(),以强制性地使wxWidgets退出,并且为下一个测试保持系统处在一个
良好的状态。
    #4 :测试方法通常以test作为前缀,尽管这处于你的控制之下(看#6)。
测试方法不要参数。我们这里的测试方法中,通过调用OnBarney事件处理器方
法来开始测试行为。
    #5 :这行使用assertEqual()方法来测试模型对象的改变是否正
确。assertEqual()要两个参数,如果这两个参数不相等,则测试失败。所有的
PyUnit断定方法都有一个可选的参数msg,如果断定失败则显示msg(msg的默认
值几乎够表达意思了)
    #6: 这个方法通过简单有效的机制创建一组测试。makeSuite()方法要求一
个Python的类的对象和一个字符串前缀作为参数,并返回一组测试(包含该类
中所有前缀为参数"前缀"的方法)。还有其它的机制,它们使得可以更明确设
置测试组中的内容,但是makeSuite()方法通过足够了。我们这里写的suite()方
法是一个样板模板,它可被用在你的所有测试模块中。
    #7 :这行调用了PyUnit的基于文本的执行器。参数是一个方法的名字(该
方法返回一测试组)。然后suite被执行,并且结果被输出到控制台。如果你想
使用GUI测试执行器,那么这行调用应使用unittest.TextTestRunner的方法而非
unittest.main。
"""

__author__ = 'tomtiddler'

import unittest

import wx

from .AUserModel import ModelExample


class TestExample(unittest.TestCase): # 1 声明一个TestCase

    def setUp(self):  # 2 为每个测试所做的配置
        self.app = wx.App()
        self.frame = ModelExample(parent=None, id=-1)

    def tearDown(self):  # 3 测试之后的清除工作
        self.frame.Destroy()

    def testModel(self): # 4 声明一个测试
        self.frame.on_barney(None)
        self.assertEqual("Barney", self.frame.model.first, msg="First is wrong")  # 5 对可能失败的断定
        self.assertEqual("Rubble", self.frame.model.last)

    def testEvent(self):
        """
        对事件的有效性进行测试，对于类似鼠标操作的一些低级事件，可以通过具体绑定该事件的部件进行测试
        。因为该鼠标时间不向上传递，所以无法直接在框架上测试
        """
        panel = self.frame.GetChildren()[0]
        for each in panel.GetChildren():
            if each.GetLabel() == "Wilmafy":
                wilma = each
                break
        event = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, wilma.GetId())
        wilma.GetEventHandler().ProcessEvent(event)
        self.assertEqual("Wilma", self.frame.model.first)
        self.assertEqual("Flintstone", self.frame.model.last)


def suite():  # 6 创建一个TestSuite
    suite = unittest.makeSuite(TestExample, "test")
    return suite


if __name__ == "__main__":
    unittest.main(defaultTest='suite')
