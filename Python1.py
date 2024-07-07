import cv2
import numpy as np
img=cv2.imread("c:\Users\DELL\Pictures\Saved Pictures\Mahesh.jpg")
gray=cv2.cvtcolor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.medianBlur(gray,5)
edges=cv2.adaptiveThreshold(gray,255,
                            cv2.ADAPTIVE_THRSH_MEAN_C,
                            cv2.THRESH_BINARY,9,9)
color=cv2.bilateralFilter(img,9,250,250)
cartoon=cv2.bitwise_and(color,color,mask=edges)
cv2.imshow('Image',img)
cv2.imshow('edges',edges)
cv2.imshow('Cartoon',cartoon)
cv2.waitkey(0)
cv2.destroyAllWindows()