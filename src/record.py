import time
import keyboard
import threading
from pynput.keyboard import Listener
import sys

class Recorder:
	def __init__(self, fps, start, pause, stop):
		self.fps = fps

		self.start = start
		self.stop = stop
		self.pause = pause

		self.running = True
		self.recording = False

		print("Listening for keys.. ")
		self.handleKeyboard()
	
	def screenshot(self):

		while self.recording:

			keyboard.press('f2')
			time.sleep(1 / self.fps)
			keyboard.release('f2')

		keyboard.release('f2')

	def handleKeyboard(self):

		while self.running:

			if keyboard.is_pressed(self.start) and not self.recording:
				print("Starting recording..")

				self.recording = True
				x = threading.Thread(target=self.screenshot)
				x.start()

			elif keyboard.is_pressed(self.pause) and self.recording:
				print("Pausing recording..")
				self.recording = False

			elif keyboard.is_pressed(self.stop):
				print("Stopping recording..")
				self.recording = False
				self.running = False

if __name__ == "__main__":
	fps = int(sys.argv[1])
	start = sys.argv[2]
	pause = sys.argv[3]
	stop = sys.argv[4]

	recorder = Recorder(fps, start, pause, stop)