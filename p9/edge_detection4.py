import math

import cv2


def hough_line_segments():
    src = cv2.imread('../imgs/1.jpeg', cv2.IMREAD_GRAYSCALE)
    if src is None:
        print('Image load failed')
        return
    edge = cv2.Canny(src, 50, 150) # image, lowerbound, upperbound
    lines = cv2.HoughLinesP(edge, 1, math.pi/180, 160, minLineLength=50, maxLineGap=5)
    dst = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    if lines is not None:
        for i in range(lines.shape[0]):
            pt1 = (lines[i][0][0], lines[i][0][1])
            pt2 = (lines[i][0][2], lines[i][0][3])
            cv2.line(dst, pt1, pt2, (0,0,255), 2, cv2.LINE_AA)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

hough_line_segments()