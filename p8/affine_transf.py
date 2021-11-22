import cv2 as cv
import numpy as np


def affine_transform_tilt():
    src = cv.imread('../imgs/tekapo.bmp')
    if src is None:
        print('Image load fail')
        return
    rows = src.shape[0]
    cols = src.shape[1]

    src_pts = np.array([[0, 0], [cols - 1, 0], [cols - 1, rows - 1]]).astype(np.float32)
    dst_pts = np.array([[50, 50], [cols - 100, 100], [cols - 50, rows - 50]]).astype(np.float32)

    affine_mat = cv.getAffineTransform(src_pts, dst_pts)
    dst = cv.warpAffine(src, affine_mat, (0, 0))

    print(affine_mat)

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


def affine_transform_move():
    src = cv.imread('../imgs/tekapo.bmp')
    if src is None:
        print('Image load fail')
        return

    affine_mat = np.array([[1, 0, 150], [0, 1, 100]]).astype(np.float32)
    dst = cv.warpAffine(src, affine_mat, (0, 0))

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


def affine_transform_shear_right():
    src = cv.imread('../imgs/tekapo.bmp')
    if src is None:
        print('Image load fail')
        return
    rows = src.shape[0]
    cols = src.shape[1]
    mv = 0.3
    affine_mat = np.array([[1, mv, 0], [0, 1, 0]]).astype(np.float32)
    dst = cv.warpAffine(src, affine_mat, (int(cols + rows * mv), rows))

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


def affine_transform_shear_down():
    src = cv.imread('../imgs/tekapo.bmp')
    if src is None:
        print('Image load fail')
        return

    rows = src.shape[0]
    cols = src.shape[1]
    mv = 0.3

    affine_mat = np.array([[1, 0, 0], [mv, 1, 0]]).astype(np.float32)
    dst = cv.warpAffine(src, affine_mat, (cols, int(rows + cols * mv)))

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()


affine_transform_tilt()
affine_transform_move()
affine_transform_shear_right()
affine_transform_shear_down()
