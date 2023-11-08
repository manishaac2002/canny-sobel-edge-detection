# canny edge detection 
import cv2 as cv

img = cv.imread('-_2003880-_URO-_20442_20200519_Kidney_0002.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 

#using this cv.canny function
canny = cv.Canny(img_gray,50,50)
cv.imshow('canny',canny)
cv.waitKey(0) 