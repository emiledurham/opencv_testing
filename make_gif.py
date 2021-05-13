import tkinter as tk
from PIL import Image, ImageTk
import os
import itertools


			
root = tk.Tk()
try:
	root.wm_attributes('-type', 'splash')
except:
	pass

size = [650, 480] 


# Dynamically change window size with left/right click

def leftclick(event): 
	size[0]+=20
	size[1]+=15

def rightclick(event):
	size[0]-=20
	size[1]-=15	


# Browse directory containing images to stitch together
gif_file = 'face_snapshots'
file_list = os.listdir(gif_file)

###############################
# feed file_list into mySort
# python's .sort() method does not work properly here


def quickSort(array):
	# Sort integers
	if len(array) < 2: # If the array has one element or is empty
		return array
	else:

		pivot = array[0] # compare each element to pivot
		lower = [i for i in array[1:] if i <= pivot]
		greater = [i for i in array[1:] if i > pivot]

	return quickSort(lower) + [pivot] + quickSort(greater) 


def stripper(array):
	newArray = []
	for string in array:
		newArray.append(string.strip('.png'))
	return newArray

myList1 = []
myList2 = []
myList3 = []

"""
steps:
1. strip .png
2. convert to int, sort
3. convert back to str, reattach .png suffix
"""

for i in stripper(file_list):
	myList1.append(int(i))
for i in quickSort(myList1):
	myList2.append(i)
for i in myList2:
	myList3.append(str(i)+'.png')

################################

images = [i for i in myList3]
images = iter(images) # iterator
images = itertools.cycle(images) # repeates iteration loop endlessly


# Main application window

class Application(tk.Frame):
	
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.master.title('opencv_to_gif')
		self.pack()	
		self.create_widgets()
		self.next_img()
		self.update()

	def next_img(self):
		"""
		Iterate through images

		"""
		try:
			self.img = next(images)
		except StopIteration:
			return


		self.img = Image.open(f'{gif_file}/{self.img}')
		self.img = self.img.resize(size)
		self.img = ImageTk.PhotoImage(self.img)
		self.bg.img = self.img
		self.bg['image'] = self.img

		
	def create_widgets(self):
		"""
		This method is called to populate the window upon startup

		"""
		self.bg = tk.Label(self)
		self.bg.pack()
		

	def update(self):
		"""
		Queue a call to this method, which in turn calls the next_img method to iterate through the gif

		"""
		self.next_img()
		# first arg is speed, lower number to increase speed
		root.after(50, self.update)




		


app = Application(master=root)
app.bg.bind("<Button-1>", leftclick)
app.bg.bind("<Button-3>", rightclick)
root.x = 650
root.y = 500
# root.resizable(0,0) # Uncomment to make window not resizable
app.mainloop()
