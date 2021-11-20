import cv2, numpy

def canny_edge():
    src = cv2.imread('../imgs/lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed')
        exit()

    dst1 = cv2.Canny(src, 50, 100)
    dst2 = cv2.Canny(src, 50, 150)

    cv2.imshow('src', src)
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)
    cv2.waitKey()
    cv2.destroyAllWindows()

canny_edge()