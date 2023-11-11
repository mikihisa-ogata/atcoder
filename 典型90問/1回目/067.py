# 067 - Base 8 to 9

import numpy as np
from functools import reduce

N_base8, K = map(int, input().split())

N_base10 = -1
N_base9 = -1
N_base9_digit = -1


for i in range(K):
    N_base10 = int(str(N_base8), 8)
    N_base9 = np.base_repr(N_base10, 9)
    N_base9_digit = [int(x) for x in list(str(N_base9))]

    for index, value in enumerate(N_base9_digit):
        if value == 8:
          N_base9_digit[index] = 5
    
    N_base8 = int(reduce(lambda x, y: x + y, [str(x) for x in N_base9_digit]))
    
print(N_base8)