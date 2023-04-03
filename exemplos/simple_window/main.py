import wx

class Window(wx.Frame):
    """
    Build a hello world window in the center of the screen
    """
    def __init__(self,title):
        super().__init__(parent=None,title=title)
        self.SetSize(400,400)
        self.Centre()
        self.Show()

app = wx.App()

window = Window("Hello, World!")

app.MainLoop()
