import tkinter as tk

class Window:
	def __init__(self, size, title="Window", icon=None, bg="white", on_close=None):
		self.size = size
		self.title = title
		self.icon = icon
		self.closeFunc = on_close

		self.window = tk.Tk()
		self.window.geometry(f"{self.size[0]}x{self.size[1]}")
		self.window.title(self.title)
		self.window.configure(bg=bg)

		if self.icon is not None: self.window.iconbitmap(self.icon)
		if self.closeFunc is not None: self.window.protocol("WM_DELETE_WINDOW", self.on_close)

	def on_close(self):
		self.closeFunc(self.window)

	def getWindowSize(self):
		w = self.window.winfo_width()
		h = self.window.winfo_height()
		return (w, h)

class Component:
	def __init__(self, window, typ, x, y, width, height, text="", callback=None, bg=None, color=None):
		self.typ = typ

		self.x = x
		self.y = y

		self.width = width
		self.height = height

		self.window = window

		self.text = text
		self.callback = callback

		if bg is None: self.bg = self.window['bg']
		self.color = color

		if self.typ == "button":
			if self.color is None:
				self.comp = tk.Button(self.window, text=self.text, command = self.callback)
			else:
				self.comp = tk.Button(self.window, text=self.text, command = self.callback, fg=self.color)
		
		elif self.typ == "text_box":

			if self.color is None:
				self.comp = tk.Entry(self.window)
			else:
				self.comp = tk.Entry(self.window, fg=self.color)

			self.comp.insert(0, str(self.text))

		elif self.typ == "label":

			if self.color is None:
				self.comp = tk.Label(self.window, text=self.text, bg=self.bg, fg="white")
			else:
				self.comp = tk.Label(self.window, text=self.text, bg=self.bg, fg=self.color)

	def place(self):
		self.comp.place()
		self.comp.place(relwidth=self.width, relheight=self.height, relx=self.x, rely=self.y)