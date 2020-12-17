import cv2
import numpy as np 
import imutils as im

cap = cv2.VideoCapture(0)

while True:
	_,img = cap.read()
	blur = cv2.GaussianBlur(img,(3,3),0)
	edges = cv2.Canny(blur,50,100)
	dilate = cv2.dilate(edges,None,iterations=1)
	cnts,_ = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	if len(cnts) != 0:
		cnt = max(cnts,key=cv2.contourArea,reverse=True)[0]
		if cv2.contourArea(cnt) >= 200:
			acc = cv2.arcLength(cnt,True)
			approx = cv2.approxPolyDP(acc,0.02*acc,True)
			if len(approx) == 4:
				print(approx)
	if cv2.waitKey(1) == ord("q"):
		break

cv2.destroyAllWindows()
cap.release()