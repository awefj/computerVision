import cv2 as cv
import numpy as np


def saturated(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0
    return value


def on_level_change(pos):
    img[:] = saturated(pos * 16)
    cv.imshow('img', img)


img = np.zeros((400, 400), np.uint8)
cv.namedWindow('img')
cv.imshow('img', img)
cv.createTrackbar('level', 'img', 0, 16, on_level_change)
cv.waitKey()
cv.destroyAllWindows()
