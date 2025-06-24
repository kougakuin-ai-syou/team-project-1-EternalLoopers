# score_stats.py
# NumPyで標準偏差・分散・相関係数などを計算

import numpy as np

def calc_std(arr):
    """列ごとの標準偏差"""
    return np.std(arr, axis=0)

def calc_var(arr):
    """列ごとの分散"""
    return np.var(arr, axis=0)

def calc_corrcoef(arr):
    """相関係数行列"""
    return np.corrcoef(arr.T)
