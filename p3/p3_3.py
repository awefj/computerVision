import numpy as np

nums = np.array([1, 4, 2, 5, 3])
ref = nums[1:4]
cpy = nums[1:4].copy()
print(ref)
print(cpy)
nums[2] = 20
print(ref)
print(cpy)