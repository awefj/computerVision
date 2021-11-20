import numpy as np

img1 = np.empty((480, 640), np.uint8)
img2 = np.zeros((480, 640, 3), np.uint8)
img3 = np.ones((480, 640), np.int32)
img4 = np.full((480, 640), 0, np.float32)

mat = np.array([[11, 12, 13, 14],
                [21, 22, 23, 24],
                [31, 32, 33, 34]]).astype(np.uint8)
mat[0, 1] = 100
mat[2, :] = 200
print(mat)