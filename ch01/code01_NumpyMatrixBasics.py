"""1.1: ndarray を使った行列計算の例

Todo:
"""

import numpy as np

# out : ndarray ... An array object satisfying the specified requirements.
A = np.array([[1, 4, -3], [-2, 1, 2]], dtype='c16')
B = np.array([[2, -3, 5], [-1, 4, 1]])

C = 2*A-3*B
print(C)

if __name__ == '__main__':
    print(type(C) is np.ndarray)
    print(C.dtype)
