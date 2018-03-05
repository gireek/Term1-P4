import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread(blah)

def warp(img):
	 img_size = (img.shape[1] , img.shape[0])

	 src = np.float32([[1 ,2] , [2 ,1] , [1 ,2] , [2 ,1] ])
	 dst = np.float32([DEFINE ACCORDING TO U])   #a desired rectangle

	 M   = cv2.getPerspectiveTransform(src , dst)
	 Minv= cv2.getPerspectiveTransform(dst , src)  #inverse matrix
	 
	 #it takes in the size we want the warped img to be, INTER_LINEAR is way to fill in missing points
	 warped = cv2.warpPerspective(img , M , img_size , flags=cv2.INTER_LINEAR)