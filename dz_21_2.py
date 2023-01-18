# Pavlo Yatluk
# dz_21_2
# Написати код, який здійснює процес перетворення матриці, наведений у прикладі з презентації.

import numpy as np
A = np.array([  [4, 2, 0],
                [1, 3, 2],
                [-1, 3, 10]])
print(A)

B = np.array([A[1], A[0], A[2]])
print(B)

C = np.array([B[0], B[1]+B[0] * (-4), B[2] + B[0]])
print(C)

D = np.array([C[0], C[1] / (-2), C[2] / 6 ], dtype=int)
print(D)

E = np.array([D[0], D[2], D[1]])
print(E)

F = np.array([E[0], E[1], E[2] + E[1] * (-5)])
print(F)