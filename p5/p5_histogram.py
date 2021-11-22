import cv2 as cv
import numpy as np


def calcGrayHist(img):
    channels = [0]
    histSize = [256]
    histRange = [0, 256]
    hist = cv.calcHist([img], channels, None, histSize, histRange)
    return hist


def getGrayHistImage(hist):
    _, histMax, _, _ = cv.minMaxLoc(hist)

    imgHist = np.ones((100, 256), np.uint8) * 255
    for x in range(imgHist.shape[1]):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
        cv.line(imgHist, pt1, pt2, 0)
    return imgHist


def createHist():
    src = cv.imread('../imgs/lenna.bmp', cv.IMREAD_GRAYSCALE)
    if src is None:
        print('Image load failed')
        return
    hist = calcGrayHist(src)
    hist_img = getGrayHistImage(hist)

    cv.imshow('src', src)
    cv.imshow('hist_img', hist_img)
    cv.waitKey()
    cv.destroyAllWindows()


def histogram_stretching():
    src = cv.imread('../imgs/lenna.bmp', cv.IMREAD_GRAYSCALE)
    if src is None:
        print('Image load failed')
        return

    gmin, gmax, _, _ = cv.minMaxLoc(src)
    dst = cv.convertScaleAbs(src, alpha=255.0 / (gmax - gmin), beta=-gmin * 255.0 / (gmax - gmin))
    cv.imshow('src', src)
    cv.imshow('srcHist', getGrayHistImage(calcGrayHist(src)))
    cv.imshow('dst', dst)
    cv.imshow('dstHist', getGrayHistImage(calcGrayHist(dst)))
    cv.waitKey()
    cv.destroyAllWindows()


def histogram_equalization():
    src = cv.imread('../imgs/lenna.bmp', cv.IMREAD_GRAYSCALE)
    if src is None:
        print('Image load failed')
        return

    dst = cv.equalizeHist(src)
    cv.imshow('src', src)
    cv.imshow('srcHist', getGrayHistImage(calcGrayHist(src)))
    cv.imshow('dst', dst)
    cv.imshow('dstHist', getGrayHistImage(calcGrayHist(dst)))
    cv.waitKey()
    cv.destroyAllWindows()


createHist()
histogram_stretching()
histogram_equalization()
