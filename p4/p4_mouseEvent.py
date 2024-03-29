import cv2 as cv
import numpy as np


def on_mouse(event, x, y, flags, param):
    global oldx, oldy

    if event == cv.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))
    elif event == cv.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' % (x, y))
    elif event == cv.EVENT_MOUSEMOVE:
        if flags & cv.EVENT_FLAG_LBUTTON:
            cv.line(img, (oldx, oldy), (x, y), (0, 0, 255), 2)
            cv.imshow('img', img)
            oldx, oldy = x, y


img = cv.imread('../imgs/lenna.bmp')
if img is None:
    print('img load failed')
    exit()

cv.namedWindow('img')
cv.setMouseCallback('img', on_mouse)
cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows()
