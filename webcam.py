import numpy as np
import cv2
import time
import os

"""
This project is:

while a face is detected by camera, take a picture each frame and save the image 
to the directory face_snapshots. when replay is pressed, feed images into make_gif.py 
and display the snapshots as a gif.

"""

# Create snapshots directory if not already created
# delete old snapshots inside directory if dir already exists
try:
	os.system('file=face_snapshots\n[ -e $file ] && { echo "proper directory exists, starting. . ."; rm -r $file/*.png; } || { mkdir $file; echo "created directory: $file"; }')
except:
	pass

cv2.namedWindow('main window') # the second arg '16' removes native buttons on top of window. Buttons include zoom in/out, screen capture. Could be useful
camera_feed = cv2.VideoCapture(0)


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')



if camera_feed.isOpened(): # grab first frame
	cam, frame = camera_feed.read()
else:
	cam = False


# This counter increments the files up as they are saved
n = 0

while cam:

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x,y,w,h) in faces:
		img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		gray_2 = gray[y:y+h, x:x+w]
		color = img[y:y+h, x:x+w]

		# This returns True while a face is detected. Since img refers to an array,
		# we must add any()/all(), meaning if anything in the array returns True, 
		# return True, or if ALL items in array return True, return True.
		if img.any():
			print('FACE DETECTED')
			# This code will read the values from camera every frame
			return_value, image = camera_feed.read()
			# Save the read value from camera
			cv2.imwrite(f'face_snapshots/{n}.png', image)
			n += 1


	cv2.imshow('main window', frame)

	cam, frame = camera_feed.read()
	key = cv2.waitKey(20)
	if key == 27: # exit on ESC
		break

cv2.destroyWindow('main window')

################################
