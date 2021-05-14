from gpiozero import LED

class Light:

	def __init__(self, color):

		self.color = LED(4)

	def turnOn(self):

		self.color.on()

	def turnOff(self, color):
		self.color.off()


