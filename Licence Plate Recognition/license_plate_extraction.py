import cv2

img = cv2.imread("./ca.jpg")


def extract_plate(img): # the function detects and perfors blurring on the number plate.
	plate_img = img.copy()
	# cv2.imshow('first',plate_img)	
	
	# Loads the data required for detecting the license plates from cascade classifier.
	plate_cascade = cv2.CascadeClassifier('./indian_license_plate.xml')

	# detects numberplates and returns the coordinates and dimensions of detected license plate's contours.
	plate_rect = plate_cascade.detectMultiScale(plate_img, scaleFactor = 1.3, minNeighbors = 7)

	for (x,y,w,h) in plate_rect:
		a,b = (int(0.02*img.shape[0]), int(0.025*img.shape[1])) #parameter tuning
		plate = plate_img[y+a:y+h-a, x+b:x+w-b, :]
		# finally representing the detected contours by drawing rectangles around the edges.
		cv2.rectangle(plate_img, (x,y), (x+w, y+h), (51,51,255), 3)
		cv2.imshow('hi2',plate)
		cv2.imwrite('messigray.png',plate)

	cv2.imshow('hi',plate_img)	
    
    

	# return plate_img, plate # returning the processed image.
extract_plate(img)	
cv2.imshow("image", img)
cv2.waitKey(0)
