import cv2
import numpy as np 
import imutils as im

cap = cv2.VideoCapture(0)
kernel = np.ones((7,7),np.uint8)
points = []
paper = None

def persp(points):
	global img
	tl,tr,br,bl = points
	width = np.sqrt(((tl[1]-tr[1])**2) + ((tl[0]-tr[0])**2))
	height = np.sqrt(((tl[1]-bl[1])**2) + ((tl[0]-bl[0])**2))
	dts = np.array([[0,0],[width,0],[width,height],[0,height]],dtype=np.float32)
	src = np.array([points],dtype=np.float32)
	M = cv2.getPerspectiveTransform(src,dts)
	warped = cv2.warpPerspective(img,M,(int(width),int(height)))
	return warped

while True:
	points = []
	_,img = cap.read()
	blur = cv2.GaussianBlur(img,kernel.shape,0)
	dilate = cv2.dilate(blur,kernel,iterations=1)
	gray = cv2.cvtColor(dilate,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,100,150)
	cnts,_ = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	if len(cnts) != 0:
		cnt = sorted(cnts,key=cv2.contourArea,reverse=True)[0]
		if cv2.contourArea(cnt) >= 200:
			acc = cv2.arcLength(cnt,True)
			approx = cv2.approxPolyDP(cnt,0.02*acc,True)
			if len(approx) == 4:
				for app in approx:
					cv2.circle(img,tuple(app[0]),10,(0,255,0),-1)
					points.append(app[0])
				paper = persp(points)
				cv2.imshow("paper",paper)
					
	cv2.imshow("img",img)
	cv2.imshow("edges",edges)
	if cv2.waitKey(1) == ord("q"):
		break

cv2.destroyAllWindows()
cap.release()