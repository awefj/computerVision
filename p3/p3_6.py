import cv2 as cv

img1 = cv.imread('../imgs/lenna.bmp')
img2 = img1[200:400, 200:400]
# img3 = img1[200:400, 200:400].copy()
img3 = img2.copy()

# img1[200:400, 200:400] = ~img2 #working
img2[:] = 255 - img2  # working - select all range of img2
# img2 = ~img2 #not working
# img2 = np.invert(img2) #not working

cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('img3', img3)
cv.waitKey()
cv.destroyAllWindows()
