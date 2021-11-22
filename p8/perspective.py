import cv2
import numpy


def on_mouse(event, x, y, flags, param):
    global cnt, src_pts
    if event == cv2.EVENT_LBUTTONDOWN:
        if cnt < 4:
            src_pts[cnt, :] = numpy.array([x, y]).astype(numpy.float32)
            cnt += 1

            cv2.circle(src, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow('src', src)
        if cnt == 4:
            w = 200
            h = 300
            dst_pts = numpy.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]]).astype(numpy.float32)

            pers_mat = cv2.getPerspectiveTransform(src_pts, dst_pts)
            dst = cv2.warpPerspective(src, pers_mat, (w, h))
            cv2.imshow('dst', dst)


cnt = 0
src_pts = numpy.zeros([4, 2], dtype=numpy.float32)
src = cv2.imread('../imgs/tekapo.bmp')
if src is None:
    print('Image load failed')
    exit()

cv2.namedWindow('src')
cv2.setMouseCallback('src', on_mouse)

cv2.imshow('src', src)
cv2.waitKey(0)
cv2.destroyAllWindows()
