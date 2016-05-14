#to run the python code on the terminal
#python AttendanceFaceRecognition.py AttendanceImages/classpicture1.jpg IT1 Z

import os
import cv2
import sys
import glob
import time
import MySQLdb
import numpy as np
from PIL import Image
import xml.etree.cElementTree as ET


# Getting the values from the GUI
imagePath = sys.argv[1]
subject = sys.argv[2]
section = sys.argv[3]
# Setting the date and time
date = time.strftime("%x")
date2 = time.strftime("%Y-%m-%d")
timestamp = time.strftime("%X")

#Loading and showing the image
img = cv2.imread(imagePath)
cv2.imshow('Attendance Image', img)
# Setting the Haar Cascade provided by OpenCV: Path where the Haar Cascade is located
# If the Haar Cascade is just within the folder of the codes:  face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


### FACE RECOGNITION SECTION ###

# Training data
# For face recognition we will the the LBPH Face Recognizer 
recognizer = cv2.face.createLBPHFaceRecognizer()
# Path where the training data set is located
loc = subject + "-" + section
path = os.path.join("./TrainingFaces",loc)

image_paths = [os.path.join(path,f) for f in os.listdir(path)]
images = []
labels = []

# Going through all the images in the data set
for image_path in image_paths:
    # Transforming the images into greyscaled and its data type
	image_pil = Image.open(image_path).convert('L')
	image = np.array(image_pil, 'uint8')
    # Getting the number of the subject being trained
	nbr = int(os.path.split(image_path)[1].split(".")[0].split(" ")[0].replace("subject", ""))
	
    # Detecting the face in the image data set
	tfaces = face_cascade.detectMultiScale(image, 1.1, 6)
	for(x,y,w,h) in tfaces:
		images.append(image[y:y+h, x:x+w])
		labels.append(nbr)
		cv2.imshow("Adding faces to training set ... ", image[y:y+h, x:x+w])
        # Cropping, saving the faces detected in the specified path
		# cv2.imwrite(os.path.join('./TrainedFaces',os.path.split(image_path)[1]), image[y:y+h, x:x+w])				
		cv2.waitKey(50)

# Using the images processed above to train the recognizer
recognizer.train(images, np.array(labels))


### FACE DETECTION SECTION ###
# Transforming the attendance image for face detection
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
attendanceimage_pil = Image.open(imagePath).convert('L')
attendanceimage = np.array(attendanceimage_pil, 'uint8')
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
recognized = []
count = 0

# Going through all the faces detected in the attendance image
for (x,y,w,h) in faces:

    # Getting the predicted subject of the recognizer and its confidence level
    nbr_predicted, conf = recognizer.predict(attendanceimage[y:y+h, x:x+w])
    print(nbr_predicted)
    print(conf) 

    # The higher the confidence level, the lower its accuracy
    # Setting the confidence level threshold to 50
    if conf > 40:
    	print("Face not recognized")
    else:
         # Putting a box on the faces detected
        cv2.rectangle(attendanceimage,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = attendanceimage[y:y+h, x:x+w]  
    	#cv2.imshow("Recognizing Face", attendanceimage[y: y + h, x: x + w])
        cv2.putText(attendanceimage, str(nbr_predicted), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 5)
    	print("Face recognized!!!")
        recognized.append(nbr_predicted)
    	count += 1
    	
print "Found {0} faces!".format(len(faces))
print "Recognized {0} faces!".format(count)

# Saving the boxed detected faces in the folder DetectedFaces
# Filename: DetectedFaces/<subject>-<section>-<date>-<time>.jpg
filename = "DetectedFaces/" + subject + "-" + section + "-"  + date2 + "-" +  timestamp + ".jpg"
cv2.imwrite(filename,attendanceimage)


### DATA SAVING SECTION ###

db = MySQLdb.connect("localhost", "root", "root", "attendancemonitoringsystem")
cursor = db.cursor()

for x in recognized:
    cursor.execute('INSERT INTO ATTENDANCE (student_id, subject, section, attendance_date) VALUES ("%s", "%s", "%s", "%s")' %\
        (x,subject,section,date2))
    try:
        db.commit()
    except: 
        db.rollback()

db.close()

cv2.waitKey(0)
cv2.destroyAllWindows()

#REFERENCES:
#http://hanzratech.in/2015/02/03/face-recognition-using-opencv.html
#http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html#face-detection
