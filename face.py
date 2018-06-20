import numpy as np
import cv2

cascPath = "/home/skanda/python/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
eyeCascade = cv2.CascadeClassifier("/home/skanda/opencv/data/haarcascades/haarcascade_eye.xml")
frame = cv2.imread('./images/cric.jpg')

#while(True):
# Capture frame-by-frame
#frame = cap.reaa
print frame
# Our operations on the frame come here
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
	gray,
	scaleFactor=1.5,
	minNeighbors=5,
	minSize=(30, 30),
	flags=cv2.CASCADE_SCALE_IMAGE
)
i = 0
font = cv2.FONT_HERSHEY_SIMPLEX
for (x, y, w, h) in faces:
	i = i+1
	cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	roi = frame[y:y+h, x:x+w]
	eyes = eyeCascade.detectMultiScale(roi)
	for (a,b,c,d) in eyes:
		cv2.rectangle(roi, (a,b), (a+c,b+d), (255, 255, 0), 2)
cv2.putText(frame, 'FACES = ' + str(i), (230, 50), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

# Display the resulting frame
while True:
	cv2.imshow('frame',frame)
	if cv2.waitKey(100) & 0xFF == ord('q'):
		cv2.destroyAllWindows()

# When everything done, release the capture
#cap.release()
#