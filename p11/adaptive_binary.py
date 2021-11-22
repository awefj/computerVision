import cv2


def on_thres(pos):
    bsize = pos
    if bsize % 2 == 0: bsize = bsize - 1
    if bsize < 3: bsize = 3
    dst = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, bsize, 5)
    cv2.imshow('dst', dst)


filename = '../imgs/sudoku.jpg'
src = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
if src is None:
    print('Image load failed')
    exit()
cv2.imshow('src', src)

cv2.namedWindow('dst')
cv2.createTrackbar('Threshold', 'dst', 0, 255, on_thres)
cv2.setTrackbarPos('Threshold', 'dst', 11)

cv2.waitKey()
cv2.destroyAllWindows()
