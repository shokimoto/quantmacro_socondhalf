# model.py

import numpy as np

# パラメータ
gamma = 2.0
beta = 0.985 ** 20
r = 1.025 ** 20 - 1
asset_grid = np.linspace(0, 10, 100)  # 資産グリッド

# 生産性タイプ（若年期）
productivity_types = [0.8027, 1.0, 1.2457]


