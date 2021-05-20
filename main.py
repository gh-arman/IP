#HISTOGRAM
import cv2 as cv
import numpy
import math



img = cv.imread("./moon.jpg", cv.IMREAD_GRAYSCALE)
height, width = img.shape
resultImg = img.copy()
pixelsCount = height*width
grayLevels = []

for i in range(0,256):
    grayLevels.append(0)

#Faravani
for i in range(0,height):
    for j in range(0, width):        
        grayLevels[img[i,j]] += 1

#Normal Sazi & ....
sum = 0
for i in range(0,256):
    sum += grayLevels[i] / pixelsCount
    grayLevels[i] = round((sum * 255))

#Make Image
for i in range(0,height):
    for j in range(0,width):
        resultImg[i,j] = grayLevels[resultImg[i,j]]

cv.imwrite("./moon2.png",resultImg)
# cv.imwrite("./moon2.jpg",tempImg)