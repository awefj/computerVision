import cv2
import numpy


def color_inverse():
    src = cv2.imread('../imgs/lenna.bmp', cv2.IMREAD_COLOR)

    if src is None:
        print('Image load failed')
        return

    dst = numpy.zeros(src.shape, src.dtype)

    for j in range(src.shape[0]):
        for i in range(src.shape[1]):
            p1 = src[j,i]
            p2 = dst[j,i]

            p2[0] = 255-p1[0]
            p2[1] = 255-p1[1]
            p2[2] = 255-p1[2]

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

color_inverse()
