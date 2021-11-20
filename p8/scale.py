import cv2 as cv
def affine_scale():
    src = cv.imread('../imgs/tekapo.bmp')

    if src is None:
        print('Image load failed')
        return
    dst1 = cv.resize(src, (0,0), fx=4, fy=4, interpolation=cv.INTER_NEAREST)
    dst2 = cv.resize(src, (1920, 1280))
    dst3 = cv.resize(src, (1920, 1280), interpolation=cv.INTER_CUBIC)
    dst4 = cv.resize(src, (1920, 1280), interpolation=cv.INTER_LANCZOS4)

    cv.imshow('src', src)
    cv.imshow('dst1', dst1[400:800, 500:900])
    cv.imshow('dst2', dst2[400:800, 500:900])
    cv.imshow('dst3', dst3[400:800, 500:900])
    cv.imshow('dst4', dst4[400:800, 500:900])

    cv.waitKey()
    cv.destroyAllWindows1()

affine_scale()