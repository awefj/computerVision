import cv2


def affine_filp():
    src = cv2.imread('../imgs/tekapo.bmp')
    if src is None:
        print('Image load failed')
        return

    cv2.imshow('src', src)

    for flip_code in [1,0,-1]:
        dst = cv2.flip(src, flip_code)

        desc = 'flipcode: %d' % flip_code
        cv2.putText(dst,desc,(10,30),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,0,0),1,cv2.LINE_AA)

        cv2.imshow('dst', dst)
        cv2.waitKey()
    cv2.destroyAllWindows()

affine_filp()