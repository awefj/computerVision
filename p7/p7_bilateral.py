import cv2
import numpy as np

src = cv2.imread('../imgs/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed')
    exit()

noise = np.zeros(src.shape, np.int32)
cv2.randn(noise, 0, 5)
cv2.add(src, noise, src, dtype=cv2.CV_8UC1)

dst1 = cv2.GaussianBlur(src, (0, 0), 5)
dst2 = cv2.bilateralFilter(src, -1, 10, 5)

cv2.imshow('src', src)  # noise
cv2.imshow('dst1', dst1)  # gaussian filter - blurred
cv2.imshow('dst2', dst2)  # bilateral filter - sharped
cv2.waitKey()
cv2.destroyAllWindows()
