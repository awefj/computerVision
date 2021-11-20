import cv2 as cv

def mask_setTo():
    src = cv.imread('../imgs/lenna.bmp', cv.IMREAD_COLOR)
    mask = cv.imread('../imgs/mask_smile.bmp', cv.IMREAD_GRAYSCALE)

    if src is None or mask is None:
        print('img load failed')
        return

    src[mask>0] = (0,255,255)
    cv.imshow('src', src)
    cv.imshow('mask', mask)
    cv.waitKey()
    cv.destroyAllWindows()

def mask_copyTo():
    src = cv.imread('../imgs/airplane.bmp', cv.IMREAD_COLOR)
    mask = cv.imread('../imgs/mask_plane.bmp', cv.IMREAD_GRAYSCALE)
    dst = cv.imread('../imgs/field.bmp', cv.IMREAD_COLOR)

    if src is None or mask is None or dst is None:
        print('img load failed')
        return
    dst[mask>0] = src[mask>0]
    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.imshow('mask', mask)
    cv.waitKey()
    cv.destroyAllWindows()

mask_setTo()
mask_copyTo()