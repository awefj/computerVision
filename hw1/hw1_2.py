import cv2 as cv
import numpy as np

img = cv.imread('../imgs/lenna.bmp', cv.IMREAD_GRAYSCALE)
if img is None:
    print('image load failed')
    exit()

img2 = img[200:400, 200:400]  # img[200:400, 200:400]부분
# img2 += 50  # 50만큼 밝게 처리, uint8값 범위(0~255)를 넘어가는 부분이 생김.
# img2 = np.clip(img2+50,0,255) #img2 += 50과 동일 결과.
# img2 = cv.add(img2, 50) #img에 적용안됨 - shallow copy 미적용. id가 달라짐.
img[200:400, 200:400] = cv.add(img2, 50)  # 원하는 결과 도출.

cv.imwrite('../imgs/lenna_50.bmp', img)  # 수정된 img를 lenna_50.bmp로 저장

cv.imshow('output', img)
cv.imshow('modified', img2)
cv.waitKey()
cv.destroyAllWindows()
