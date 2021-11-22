import cv2, numpy


def sobel_edge():
    src = cv2.imread('../imgs/lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed')
        exit()

    dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
    dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

    fmag = cv2.magnitude(dx, dy)
    mag = numpy.uint8(numpy.clip(fmag, 0, 255))
    _, edge = cv2.threshold(mag, 150, 255, cv2.THRESH_BINARY)

    cv2.imshow('src', src)
    cv2.imshow('mag', mag)
    cv2.imshow('edge', edge)
    cv2.waitKey()
    cv2.destroyAllWindows()


sobel_edge()
