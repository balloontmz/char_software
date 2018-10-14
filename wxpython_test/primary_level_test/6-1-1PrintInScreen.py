#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
简单的绘画窗口，代码来自复制。
    #1:wx.Pen实例决定绘画到设备上下文的线条的颜色、粗细和样式。样式
除了wx.SOLID还有wx.DOT, wx.LONGDASH, 和wx.SHORTDASH。
    #2:窗口需要去响应几个不同的鼠标类型事件以便绘制图形。响应的事件
有鼠标左键按下和释放、鼠标移动、窗口大小变化和窗口重绘。这里也指定了
空闲时的处理。
    #3:用两步创建了缓存的设备上下文:(1)创建空的位图,它作为画面
外(offscreen)的缓存(2)使用画面外的缓存创建一个缓存的设备上下文。这个
缓存的上下文用于防止我勾画线的重绘所引起的屏幕闪烁。在这节的较后面的
部分,我们将更详细地讨论这个缓存的设备上下文。
    #4:这几行发出绘制命令到设备上下文;具体就是,设置背景色并清空设
备上下文(dc.Clear())。必须调用dc.Clear(),其作用是产生一个wx.EVT_PAINT
事件,这样,设置的背景就显示出来了,否则屏幕颜色不会改变。wx.Brush对
象决定了背景的颜色和样式。
    #5:事件方法GetPositionTuple()返回一个包含鼠标敲击的精确位置的
Python元组。
    #6:CaptureMouse()方法控制了鼠标并在窗口的内部捕获鼠标,即使是你
拖动鼠标到窗口边框的外面,它仍然只响应窗口内的鼠标动作。在程序的后面
必须调用ReleaseMouse()来取消其对鼠标的控制。否则该窗口将无法通过鼠标
关闭等,试将#7注释掉。
    #7:ReleaseMouse()方法将系统返回到调用CaptureMouse()之前的状
态。wxPython应用程序使用一个椎栈来对捕获了鼠标的窗口的跟踪,调用
ReleaseMouse()相当于从椎栈中弹出。这意味着你需要调用相同数据的
CaptureMouse()和ReleaseMouse()。
    #8:这行确定移动事件是否是线条绘制的一部分,由移动事件发生时鼠标
左键是否处于按下状态来确定。Dragging()和LeftIsDown()都是wx.MouseEvent
的方法,如果移动事件发生时所关联的条件成立,方法返回true。
    #9:由于wx.BufferedDC是一个临时创建的设备上下文,所以在我们绘制
线条之前需要另外创建一个。这里,我们创建一个新的wx.ClientDC作为主要的
设备上下文,并再次使用我们的实例变量位图作为缓存。
    #10:这几行实际是使用设备上下文去绘画新近的勾画线到屏幕上。首
先,我们创建了coords元组,它合并了self.pos和newPos元组。这里,新的位置
来自于事件GetPositionTuple(),老的位置是最后对OnMotion()调用所得到的。
我们把该元组保存到self.curLine列表中,然后调用DrawLine()。*coords返回元
组coords中的元素x1,y1,x2,y2。DrawLine()方法要求的参数形如x1,y1,x2,y2,并
从点(x1,y1)到(x2,y2)绘制一条线。勾画的速度依赖于底层系统的速度。
    #11:如果窗口大小改变了,我们存储一个True值到self.reInitBuffer实例属
性中。我们实际上不做任何事直到下一个空闲事件。
    #12:当一个空闲产生时,如果已发生了一个或多个尺寸改变事件,这个
应用程序抓住时机去响应一个尺寸改变事件。我们存储一个True值到
self.reInitBuffer实例属性中,并在一个空闲产生时响应的动机是避免对于接二
连三的尺寸改变事件都进行屏幕刷新。
    #13:对于所有的显示要求,都将产生wx.EVT_PAINT事件(描绘事件),
并调用我们这里的方法OnPaint进行屏幕刷新(重绘),你可以看到这是出乎意
料的简单:创建一个缓存的画图设备上下文。实际上wx.PaintDC被创建(因为
我们处在一个Paint请求里,所以我们需要wx.PaintDC而非一个wx.ClientDC实
例),然后在dc实例被删除后(函数返回时被销毁),位图被一块块地传送
(blit)给屏幕并最终显示。关于缓存的更详细的信息将在随后的段落中提供。
    #14:当由于尺寸改变(和由于从文件载入)而导致应用程序需要根据实
际数据重绘线条时,被使用。这里,我们遍历存储在实例变量self.lines中行的
列表,为每行重新创建画笔,然后根据坐标绘制每一条线。
"""

__author__ = 'tomtiddler'

import os
import json

import wx


class SketchWindow(wx.Window):
    def __init__(self, parent, ID):
        super(SketchWindow, self).__init__(parent, ID)
        self.SetBackgroundColour("White")
        self.color = "Black"
        self.thickness = 1
        self.pen = wx.Pen(self.color, self.thickness, style=wx.PENSTYLE_SOLID)  # 1 创建一个wx.Pen对象
        self.lines = []
        self.curLine = []
        self.pos = (0, 0)
        self.InitBuffer()
        # 2 连接事件
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMotion)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def InitBuffer(self):
        size = self.GetClientSize()
        # 3 创建一个缓存的设备上下文
        self.buffer = wx.Bitmap(size.width, size.height)
        dc = wx.BufferedDC(None, self.buffer)
        # 4 使用设备上下文
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        self.DrawLines(dc)
        self.reInitBuffer = False

    def GetLinesData(self):
        return self.lines[:]

    def SetLinesData(self, lines):
        self.lines = lines[:]
        self.InitBuffer()
        self.Refresh()

    def OnLeftDown(self, event):
        self.curLine = []
        self.pos = event.GetPosition()  # 5 得到鼠标的位置
        self.CaptureMouse()  # 6 捕获鼠标

    def OnLeftUp(self, event):
        if self.HasCapture():
            self.lines.append((self.color,
                               self.thickness,
                               self.curLine))
            self.curLine = []
            self.ReleaseMouse()  # 7 释放鼠标

    def OnMotion(self, event):
        if event.Dragging() and event.LeftIsDown():  # 8 确定是否在拖动
            dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)  # 9 创建另一个缓存的上下文
            self.drawMotion(dc, event)
        event.Skip()

    # 10 绘画到设备上下文
    def drawMotion(self, dc, event):
        dc.SetPen(self.pen)
        newPos = event.GetPosition()
        coords = (self.pos, newPos)  # 此行代码有问题，但是，将两个truple合并成一个更大的truple应该怎么操作呢
        self.curLine.append(coords)
        dc.DrawLine(*coords)
        self.pos = newPos

    def OnSize(self, event):
        self.reInitBuffer = True  # 11 处理一个resize事件

    def OnIdle(self, event):  # 12 空闲时的处理
        if self.reInitBuffer:
            self.InitBuffer()
            self.Refresh(False)

    def OnPaint(self, event):
        dc = wx.BufferedPaintDC(self, self.buffer)  # 13 处理一个paint(描绘)请求

    # 14 绘制所有的线条
    def DrawLines(self, dc):
        for colour, thickness, line in self.lines:
            pen = wx.Pen(colour, thickness, style=wx.PENSTYLE_SOLID)
            dc.SetPen(pen)
            for coords in line:
                dc.DrawLine(*coords)

    def SetColor(self, color):
        self.color = color
        self.pen = wx.Pen(self.color, self.thickness, style=wx.PENSTYLE_SOLID)

    def SetThickness(self, num):
        self.thickness = num
        self.pen = wx.Pen(self.color, self.thickness, style=wx.PENSTYLE_SOLID)


class SketchFrame(wx.Frame):
    """
    #1:现在__init__方法包含了更多的功能,我们把状态栏放在了它自己的方
法中。
    #2:菜单数据的格式现在是(标签, (项目)),其中的每个顶目也是一个列表
(标签, 描术文字, 处理器, 可选的kind)或一个带有标签和项目的菜单。确定数据
的一个子项目是菜单还是一个菜单项,请记住,菜单的长度是2,项目的长度
是3或4。对于更复杂的产品数据,我建议使用XML或别的外部格式。
    #3:如果数据块的长度是2,这意味它是一个菜单,将之分开,并递归调
用createMenu,然后将之添加。
    #4:创建菜单项。对wx.MenuItem的构造器使用kind参数的方法比使用
wx.Menu的特定方法更容易。
    #5:OnColor方法根据所选菜单项来改变画笔的颜色。代码根据事件得到
项目的id,再使用FindItemById()来得到正确的菜单项(注意我们这里使用菜单
栏作为数据结构来访问,而没有使用项目id的哈希表),这个方法是以标签是
wxPython颜色名为前提的。
    """
    def __init__(self, parent):
        self.title = "Tomtiddler"
        super(SketchFrame, self).__init__(parent, -1, self.title, size=(800, 600))
        self.filename = ""
        self.wildcard = wx.FileSelectorDefaultWildcardStr
        self.sketch = SketchWindow(self, -1)
        self.sketch.Bind(wx.EVT_MOTION, self.OnSketchMotion)

        self.statusbar = self.initStatusBar()

        self.createMenuBar()

    def initStatusBar(self):
        statusbar = self.CreateStatusBar()
        statusbar.SetFieldsCount(3)
        statusbar.SetStatusWidths([-1, -2, -3])
        return statusbar

    def OnSketchMotion(self, event):
        self.statusbar.SetStatusText("Pos: %s" % str(event.GetPosition()), 0)
        self.statusbar.SetStatusText("Current Pts: %s" % len(self.sketch.curLine), 1)
        self.statusbar.SetStatusText("Line Count: %s" % len(self.sketch.lines), 2)
        event.Skip()

    def menuData(self):
        return [("&File",
                 (("&New", "New Sketch file", self.OnNew),
                  ("&Open", "Open sketch file", self.OnOpen),
                  ("&Save", "Save sketch file", self.OnSave),
                  ("", "", ""),
                  (" & Color", (
                    (" & Black", "", self.OnColor,
                     wx.ITEM_RADIO),
                    (" & Red", "", self.OnColor,
                     wx.ITEM_RADIO),
                    (" & Green", "", self.OnColor,
                     wx.ITEM_RADIO),
                    (" & Blue", "", self.OnColor,
                     wx.ITEM_RADIO),
                    (" & Other...", "", self.OnOtherColor,
                     wx.ITEM_RADIO))),
                  ("", "", ""),
                  (" & Quit", "Quit", self.OnCloseWindow))
                 )]

    def createMenuBar(self):
        menubar = wx.MenuBar()
        for eachMenuData in self.menuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1]
            menubar.Append(self.createMenu(menuItems), menuLabel)
        self.SetMenuBar(menubar)

    def createMenu(self, menuData):
        menu = wx.Menu()
        for eachItem in menuData:
            if len(eachItem) == 2:
                label = eachItem[0]
                subItem = self.createMenu(eachItem[1])
                menu.Append(wx.NewIdRef(), label, subItem)

            else:
                self.createMenuItem(menu, *eachItem)
        return menu

    def createMenuItem(self, menu, label, status, handler, kind=wx.ITEM_NORMAL):
        if not label:
            menu.AppendSeparator()
            return
        menuItem = menu.Append(-1, label, status, kind)
        self.Bind(wx.EVT_MENU, handler, menuItem)

    def OnNew(self): pass

    def OnOpen(self, event):
        dlg = wx.FileDialog(self, " Open sketch file...", os.getcwd(), style=wx.FD_OPEN, wildcard=self.wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.ReadFile()
            self.SetTitle(self.title + "--" + self.filename)
        dlg.Destroy()

    def ReadFile(self):
        if self.filename:
            try:
                with open(self.filename, "r") as fi:
                    data = fi.read()
                    data = json.loads(data)
                temp, index = data, 0
                for po1, po2 in data[0][2]:
                    temp[0][2][index] = (wx.Point(po1[0], po1[1]), wx.Point(po2[0], po2[1]))
                    index += 1
                self.sketch.SetLinesData(temp)
            except Exception as e:
                wx.MessageBox("%s is not a file" % self.filename, "oops!", style=wx.OK|wx.ICON_EXCLAMATION)

    def OnSave(self, event):
        if not self.filename:
            self.OnSaveAs(event)
        else:
            self.SaveFile()

    def OnSaveAs(self, event):
        dlg = wx.FileDialog(self, "Save sketch as ...",
                            os.getcwd(),
                            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT,
                            wildcard=self.wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            self.filename = filename
            self.SaveFile()
            self.SetTitle(self.title + "--" + self.filename)
        dlg.Destroy()

    def SaveFile(self):
        if self.filename:
            data = self.sketch.GetLinesData()
            temp, index = data, 0
            for po1, po2 in data[0][2]:
                temp[0][2][index] = ((po1[0], po1[1]), (po2[0], po2[1]))
                index += 1
            with open(self.filename, "w") as fi:
                data = json.dumps(temp)
                fi.write(data)

    def OnColor(self, event):
        menubar = self.GetMenuBar()
        itemId = event.GetId()
        item = menubar.FindItemById(itemId)
        color = item.GetLabel()
        self.sketch.SetColor(color)

    def OnOtherColor(self, event):
        """
        如果用户能够在sketch对话框中选择任意的颜色,那么这将是有用。对于
这个目的,我们可以使用wxPython提供的标准wx.ColourDialog。这个对话框的
用法类似于文件对话框。它的构造器只需要一个parent(双亲)和一个可选的数据
属性参数。数据属性是一个wx.ColourData的实例,它存储与该对话框相关的一
些数据,如用户选择的颜色,还有自定义的颜色的列表。使用数据属性使你能
够在以后的应用中保持自定义颜色的一致性。
在sketch应用程序中使用颜色对话框,要求增加一个菜单项和一个处理器
方法。例6.7显示了所增加的代码。
        :param event:
        :return:
        """
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True)  # 创建颜色数据对象
        if dlg.ShowModal() == wx.ID_OK:
            self.sketch.SetColor(dlg.GetColourData().GetColour())  # 根据用户的输入设置颜色
        dlg.Destroy()

    def OnCloseWindow(self, event):
        self.Destroy()


if __name__ == "__main__":
    app = wx.App()
    frame = SketchFrame(None)
    frame.Show(True)
    app.MainLoop()
