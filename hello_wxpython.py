import wx
class MyApp(wx.App):
	#弹出框显示内容
	def OnInit (self):
		wx.MessageBox ("Hello wxpython","wxApp")
		return True
if __name__ == '__main__':
	app = MyApp(False)
	app.MainLoop()
