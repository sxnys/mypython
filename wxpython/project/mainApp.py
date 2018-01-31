# coding: utf-8

import wx
# import Frame1
import mainFrame
from extra import JsonIO

class MainApp(wx.App):
    def OnInit(self):
        # raw_input()
        self.frame = mainFrame.MainWindow(None, u'国防科技卓越青年人才基金项目申报')
        self.frame.Show()

        # print JsonIO.getNewJsonDict()
        return True

if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()