import cv2 as cv
import numpy as np

def time_inverse():
    src = cv.imread('../imgs/lenna.bmp', cv.IMREAD_COLOR)
    if src is None:
        print('image load failed')
        return
    dst = np.empty(src.shape, dtype=src.dtype)

    tm = cv.TickMeter()

    tm.start()
    for y in  range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y,x] = ~src[y, x]
    tm.stop()

    print('image inverse implementation took %4.3f ms.' % tm.getTimeMilli())

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()

def time_inverse_improved():
    src = cv.imread('../imgs/lenna.bmp', cv.IMREAD_COLOR)
    if src is None:
        print('image load failed')
        return
    dst = np.empty(src.shape, dtype=src.dtype)

    tm = cv.TickMeter()

    tm.start()
    dst = ~src
    tm.stop()

    print('image inverse implementation took %4.3f ms.' % tm.getTimeMilli())

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()

time_inverse()
time_inverse_improved()