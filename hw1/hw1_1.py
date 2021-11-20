import cv2 as cv

img = cv.imread('../imgs/lenna.bmp', cv.IMREAD_GRAYSCALE)
if img is None:
    print('image load failed')
    exit()
img1 = img[200:400, 200:400]  # img[200:400, 200:400]부분
img1 += 20  # 20만큼 밝게 처리

cv.imwrite('../imgs/lenna_20.bmp', img)  # 수정된 img를 lenna_20.bmp로 저장

cv.imshow('output', img)
cv.imshow('modified', img1)
cv.waitKey()
cv.destroyAllWindows()
