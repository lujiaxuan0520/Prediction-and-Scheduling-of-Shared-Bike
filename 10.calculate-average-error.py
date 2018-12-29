# coding=utf-8
import math
import numpy as np

# 计算平均误差
predict_result = np.loadtxt("predict_result.txt")
predict_result.reshape(4000, 1)
test_output_arr=np.load("test_output_arr.npy")
ntest_output_arr=[]
for i in range(len(test_output_arr)):
    ntest_output_arr.append(test_output_arr[i][0])
ntest_output_arr = np.array(ntest_output_arr)
avg_error = (np.abs(predict_result - ntest_output_arr)) / ntest_output_arr
avg_error = np.mean(avg_error)
print('平均误差：', str(avg_error))
