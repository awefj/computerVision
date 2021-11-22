import sys
import cv2
import numpy as np

argc = len(sys.argv)
if argc < 3:
    print('Usage : stiching.exe <image_file1> <image_file2> [<image_file3> ...]')
    sys.exit()

imgs = []
for i in range(1, argc):
    img = cv2.imread(sys.argv[i])
    if img is None:
        print('Image load failed')
        sys.exit()

    imgs.append(img)

stitcher = cv2.Stitcher_create()
status, dst = stitcher.stich(imgs)

if status != cv2.STITCHER_OK:
    print('Error on stitching')
    sys.exit()
cv2.imwrite('result.jpg', dst)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
