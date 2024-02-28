import wx

class TransparentFrame(wx.Frame):
    def __init__(self):
        style = (wx.FRAME_NO_TASKBAR | wx.NO_BORDER | wx.STAY_ON_TOP)
        super().__init__(None, style=style)

        self.Maximize(True)

        self.SetTransparent(100)

        panel = wx.Panel(self)
        panel.SetBackgroundColour(wx.Colour(0,0,0,0))

        button = wx.Button(panel, label="Close")
        button.Bind(wx.EVT_BUTTON, self.on_close)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddStretchSpacer()
        sizer.Add(button, 0, wx.ALIGN_CENTER)
        sizer.AddStretchSpacer()
        panel.SetSizer(sizer)

    def on_close(self, event):
        self.Close()

app = wx.App()
frame = TransparentFrame()
frame.Show()
app.MainLoop()