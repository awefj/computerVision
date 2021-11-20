import cv2


def color_grayscale():
    src = cv2.imread('../imgs/lenna.bmp', cv2.IMREAD_COLOR)
    if src is None:
        print('Image load failed')
        return

    dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

color_grayscale()