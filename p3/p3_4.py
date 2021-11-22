import cv2 as cv

img1 = cv.imread('../imgs/lenna.bmp')
img2 = img1
img3 = img1.copy()

img1[:, :] = (0, 255, 255)  # B G R
cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('img3', img3)
cv.waitKey()
cv.destroyAllWindows()
