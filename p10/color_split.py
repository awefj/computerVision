import cv2


def color_split():
    src = cv2.imread('../imgs/lenna.bmp', cv2.IMREAD_COLOR)
    if src is None:
        print('Image load failed')
        return

    bgr_planes = cv2.split(src)

    cv2.imshow('src',src)
    cv2.imshow('B',bgr_planes[0])
    cv2.imshow('G',bgr_planes[1])
    cv2.imshow('R',bgr_planes[2])
    cv2.waitKey()
    cv2.destroyAllWindows()
color_split()