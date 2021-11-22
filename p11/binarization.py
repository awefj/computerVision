import cv2


def on_thres(pos):
    _, dst = cv2.threshold(src, pos, 255, cv2.THRESH_BINARY)
    cv2.imshow('dst', dst)


filename = '../imgs/neutrophils.png'

src = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
if src is None:
    print('Image load failed')
    exit()
cv2.imshow('src', src)

cv2.namedWindow('dst')
cv2.createTrackbar('Threshold', 'dst', 0, 255, on_thres)
cv2.setTrackbarPos('Threshold', 'dst', 128)

cv2.waitKey()
cv2.destroyAllWindows()
