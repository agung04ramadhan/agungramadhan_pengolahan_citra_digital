import cv2 as cv
import numpy as np

image = cv.imread('luffy.jpg')
alpha = 2 
adjusted = cv.convertScaleAbs(image, alpha=alpha)

cv.imshow('adjusted', adjusted)
cv.waitKey()
cv.destroyAllWindows()