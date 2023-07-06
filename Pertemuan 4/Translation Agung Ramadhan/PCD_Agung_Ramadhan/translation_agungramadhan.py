import cv2
import numpy as np

load = cv2.imread('agung.jpeg',1)
width, height = load.shape[1], load.shape[0]

trans = np.float32([[1,0,50], [0,1,150]])
img_trans = cv2.warpAffine(load, trans, (width, height))

cv2.imshow('image yang digeser', img_trans)

cv2.waitKey(0)
cv2.destroyAllWindows()