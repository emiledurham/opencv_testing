import tkinter as tk
from PIL import Image, ImageTk
from random import choice
import os
import itertools



root = tk.Tk()
root.wm_attributes('-type', 'splash')
size = [500, 500] 


# Dynamically change window size with left/right click

def leftclick(event): 
	size[0]+=20
	size[1]+=20

def rightclick(event):
	size[0]-=20
	size[1]-=20	


# Browse directory containing images to stitch together
gif_file = 'face_snapshots'
file_list = os.listdir(gif_file)
 # Will be unordered unless sorted

###############################
# feed file_list into mySort


def quickSort(array):
	# Sort integers
	# base case
	if len(array) < 2: # If the array has one element or is empty
		return array
	else:

		pivot = array[0] # compare each element to pivot, recursive case
		lower = [i for i in array[1:] if i <= pivot] # elements smaller than or equal to pivot
		greater = [i for i in array[1:] if i > pivot] # elements larger than pivot

	return quickSort(lower) + [pivot] + quickSort(greater) 


def mySort(array):
	# strip and sort strings, feed into quickSort function
	if len(array) < 2:
		return array
	else:
		newArray = []
		
		for string in array:
			newArray.append(string.strip('.png'))
			pivot = array[0].strip('.png')
			lower = [i for i in newArray[1:] if i <= pivot]
			greater = [i for i in newArray[1:] if i > pivot]

	return mySort(lower) + [pivot] + mySort(greater)


myList1 = []
myList2 = []
myList3 = []

for i in mySort(file_list):
	myList1.append(int(i))
for i in quickSort(myList1):
	# myList2.append(str(i)+'.png')
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
		root.after(25, self.update)




		


app = Application(master=root)
app.bg.bind("<Button-1>", leftclick)
app.bg.bind("<Button-3>", rightclick)
root.x = 500
root.y = 500
# root.resizable(0,0) # Uncomment to make window not resizable
app.mainloop()
