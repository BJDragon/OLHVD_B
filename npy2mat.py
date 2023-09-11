import numpy as np
from scipy.io import savemat

# 从.npy文件加载NumPy数组
npy_array = np.load('result.npy')

# 保存为.mat文件
savemat('OLHVD200.mat', {'size_of_SRR': npy_array})
