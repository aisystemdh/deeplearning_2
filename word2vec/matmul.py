# import numpy as np
# c = np.array([[1,0,0,0,0,0,0]])
# W = np.random.randn(7,3)

# h = np.dot(c,W)

# print(h)

import sys
sys.path.append("..")
import numpy as np
from common.layers import Matmul

c = np.array([[1,0,0,0,0,0,0]])
W =np.random.randn(7,3)
layer = MatMul(W)
h = layer.forward(c)
print(h)
