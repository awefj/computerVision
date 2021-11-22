import cv2 as cv

img = cv.imread('../imgs/lenna.bmp', cv.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed')
    exit()
print('type(img):', type(img))
print('img.shape:', img.shape)

if len(img.shape) == 2:
    print('img is a grayscale image')
elif len(img.shape) == 3:
    print('img is a truecolor image')

cv.imshow('image', img)
cv.waitKey()
cv.destroyAllWindows()
