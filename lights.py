from gpiozero import LED

class Light:

	def __init__(self, color, number):
		
		self.number = number
		self.color = LED(self.number)

	def turnOn(self):

		self.color.on()

	def turnOff(self):
		
		self.color.off()


