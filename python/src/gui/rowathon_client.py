#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Tue Aug  2 09:28:21 2011

import wx
from RowConfigure import RowConfigure

class RowathonClient(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        configuration = RowConfigure(None, -1, "")
        self.SetTopWindow(configuration)
        configuration.Show()
        return 1

# end of class RowathonClient

if __name__ == "__main__":
    rowathon_client = RowathonClient(0)
    rowathon_client.MainLoop()
