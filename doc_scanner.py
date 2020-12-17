import cv2
import numpy as np 
import imutils as im

cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
kernel = np.ones((5,5),np.uint8)

while True:
	_,img = cap.read()
	blur = cv2.GaussianBlur(img,kernel.shape,0)
	dilate = cv2.dilate(edges,kernel,iterations=1)
	gray = cv2.cvtColor(dilate,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,100,150)
	cnts,_ = cv2.findContours(egdes,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	"""if len(cnts) != 0:
		cnt = sorted(cnts,key=cv2.contourArea,reverse=True)[0]
		if cv2.contourArea(cnt) >= 200:
			acc = cv2.arcLength(cnt,True)
			approx = cv2.approxPolyDP(cnt,0.02*acc,True)
			if len(approx) == 4:
				for app in approx:
					cv2.circle(img,tuple(app[0]),10,(0,255,0),-1)"""
					
	cv2.imshow("img",edges)
	if cv2.waitKey(1) == ord("q"):
		break

cv2.destroyAllWindows()
cap.release()