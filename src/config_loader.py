import json
import ctypes
import os

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

defaultData = {
	"width" : screensize[0] / 2,
	"height" : screensize[1] / 2,
	"fps" : 20,
	"out" : "../render/video.avi",
	"start_recording" : "j",
	"pause_recording" : "k",
	"stop_recording" : "l"
}

class Config:
	def __init__(self, file):
		self.file = file

		if not os.path.isfile(self.file):
			name = os.path.basename(self.file)
			dr = self.file.replace(f"/{name}", "")
			os.makedirs(dr)
			self.data = defaultData

		else:
                        with open(self.file, "r", encoding="utf-8") as f:
                                self.data = json.loads(f.read())

	def getData(self, key):
		try:
			return self.data[key]

		except KeyError as e:

			try:
				return defaultData[key]

			except KeyError as e:
				return None

	def setData(self, key, value):
		self.data[key] = value 

	def save(self):
		with open(self.file, "w", encoding="utf-8") as f:
			f.write(json.dumps(self.data, indent=4))
