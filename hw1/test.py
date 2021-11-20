import cv2 as cv

img = cv.imread('../imgs/lenna.bmp', cv.IMREAD_GRAYSCALE)
img2 = img
img3 = img

print(id(img), id(img2), id(img3))

img2 = ~img2
img3 += 30

print(id(img), id(img2), id(img3))

cv.imshow('original', img)
cv.imshow('copy1', img2)
cv.imshow('copy2', img3)
cv.waitKey()
cv.destroyAllWindows()