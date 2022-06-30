import tkinter as tk
import threading
from config_loader import Config
from components import *
from render_vid import render
import os
from tkinter import messagebox

class App:
	def __init__(self):
		self.conf = Config("config/config.json")

		w = int(self.conf.getData("width"))
		h = int(self.conf.getData("height"))

		self.window = Window((w, h), title="Sony Vegas + OBS", icon="config/icon.ico", bg="#262626", on_close=self.on_close)
		self.fps = int(self.conf.getData("fps"))
		self.out = self.conf.getData("out")

		self.start_recording = self.conf.getData("start_recording")
		self.stop_recording = self.conf.getData("stop_recording")
		self.pause_recording = self.conf.getData("pause_recording")

		# vegas
		label = Component(self.window.window, "label", 0.05, 0.05, 0.4, 0.1, text="Fps: ")
		label.place()

		self.fpsTxt = Component(self.window.window, "text_box", 0.05, 0.2, 0.4, 0.1, text=self.fps)
		self.fpsTxt.place()

		label = Component(self.window.window, "label", 0.05, 0.35, 0.4, 0.1, text="Out file: ")
		label.place()

		self.outTxt = Component(self.window.window, "text_box", 0.05, 0.5, 0.4, 0.1, text=self.out)
		self.outTxt.place()

		# obs

		label = Component(self.window.window, "label", 0.55, 0.05, 0.4, 0.1, text="Start Recording: ")
		label.place()

		self.startRecordingTxt = Component(self.window.window, "text_box", 0.55, 0.2, 0.4, 0.1, text=self.start_recording)
		self.startRecordingTxt.place()

		label = Component(self.window.window, "label", 0.55, 0.35, 0.4, 0.1, text="Pause Recording: ")
		label.place()

		self.pauseRecordingTxt = Component(self.window.window, "text_box", 0.55, 0.5, 0.4, 0.1, text=self.pause_recording)
		self.pauseRecordingTxt.place()


		label = Component(self.window.window, "label", 0.55, 0.65, 0.4, 0.1, text="Stop Recording: ")
		label.place()

		self.stopRecordingTxt = Component(self.window.window, "text_box", 0.55, 0.8, 0.4, 0.1, text=self.stop_recording)
		self.stopRecordingTxt.place()

		# buttons

		self.renderBtn = Component(self.window.window, "button", 0.1, 0.7, 0.3, 0.1, text="Render Video", callback=self.render)
		self.renderBtn.place()

		self.recorderButton = Component(self.window.window, "button", 0.1, 0.85, 0.3, 0.1, text="Open Recorder", callback=self.record)
		self.recorderButton.place()

		self.window.window.mainloop()

	def on_close(self, window):
		try:
			size = self.window.getWindowSize()

			self.conf.setData("width", size[0])
			self.conf.setData("height", size[1])

			self.conf.setData("fps", int(self.fpsTxt.comp.get()))
			self.conf.setData("out", self.outTxt.comp.get())

			self.conf.setData("start_recording", self.startRecordingTxt.comp.get()[0])
			self.conf.setData("pause_recording", self.pauseRecordingTxt.comp.get()[0])
			self.conf.setData("stop_recording", self.stopRecordingTxt.comp.get()[0])

			self.conf.save()
		except Exception as e:
			print(e)

		window.destroy()

	def render(self):
		out = self.outTxt.comp.get()

		if os.path.isfile(out):
			answer = messagebox.askokcancel("File already exists", f"Do you really want to override this file '{out}'?")
			if not answer: return
			os.remove(out)

		x = threading.Thread(target=render, args=[out, int(self.fpsTxt.comp.get())])
		x.start()

	def record(self):
		x = threading.Thread(target=self.recordThread)
		x.start()

	def recordThread(self):

		start = self.startRecordingTxt.comp.get()[0]
		stop = self.stopRecordingTxt.comp.get()[0]
		pause = self.pauseRecordingTxt.comp.get()[0]
		fps = self.fpsTxt.comp.get()

		os.system(f"start cmd /c python record.py {fps} {start} {pause} {stop}")

def run():
	app = App()

if __name__ == "__main__":
	x = threading.Thread(target=run)
	x.start()