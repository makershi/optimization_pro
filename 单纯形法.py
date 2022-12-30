# -*- encoding: utf-8 -*-
'''
@File    :   单纯形法.py
@Time    :   2022/12/30 22:00:03
@Author  :   makershi 
'''
import pandas as pd
import numpy as np
# 定义线性规划求解函数
def lp_solver(matrix:DataFrame):# pandas 中的 DataFrame对象是二维矩阵
    """
    输入线性规划的矩阵，根据单纯形法求解线性规划模型.标准形式为：
    min C^TX
    s.t. ax=b x>=0
          x1 x2 x3 x4 b
    fx    1  2  3  -2 19
    x1    1  -2 0  4  4
    x3    0  1  1  -2 5
    第1行是目标函数的系数，其余行是约束方程的系数。
    b列是常数项，第一个是当前目标函数的值。
    x=(4,0,5,0)是初始基可行解，x1和x3是初始基向量
    :param matrix:
    :return:
    """
    # 判别数检验
    c = matrix.iloc[0,1:] # 按照行列默认数值（0,1,2...）取出对应元素