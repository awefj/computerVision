import cv2 as cv

img1 = cv.imread('../imgs/lenna.bmp', cv.IMREAD_GRAYSCALE)
img2 = img1[200:400, 200:400]
# img3 = img1[200:400, 200:400].copy() #same as img2.copy()
img3 = img2.copy()

img2 += 20

cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('img3', img3)
cv.waitKey()
cv.destroyAllWindows()
