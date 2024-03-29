import numpy as np
import cv2 as cv


def brightness1():
    src = cv.imread('../imgs/lenna.bmp', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed')
        return

    dst = cv.add(src, 100)

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


def brightness2():
    src = cv.imread('../imgs/lenna.bmp', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed')
        return

    dst = np.empty(src.shape, src.dtype)
    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y, x] = src[y, x] + 100  # overflow

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


def saturated(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0
    return value


def brightness3():
    src = cv.imread('../imgs/lenna.bmp', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed')
        return

    dst = np.empty(src.shape, src.dtype)
    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y, x] = saturated(src[y, x] + 100)  # overflow

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


def brightness4():
    src = cv.imread('../imgs/lenna.bmp', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed')
        return

    def update(pos):
        dst = cv.add(src, pos)
        cv.imshow('dst', dst)

    cv.namedWindow('dst')
    cv.createTrackbar('Brightness', 'dst', 0, 100, update)
    update(0)
    cv.waitKey()
    cv.destroyAllWindows()


brightness1()
brightness2()
brightness3()
brightness4()
