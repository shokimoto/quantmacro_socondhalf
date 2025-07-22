import numpy as np

P = np.array([
    [0.7451, 0.2528, 0.0021],
    [0.1360, 0.7281, 0.1360],
    [0.0021, 0.2528, 0.7451]
])

productivity_types = np.array([0.8027, 1.0, 1.2457])

r = 1.025 ** 20 - 1  # 利子率の計算

import numpy as np

# モデルのパラメータ
beta = 0.98520
gamma = 2.0
r = 1.02520 - 1
asset_grid = np.linspace(0, 10, 100)  # 資産グリッド
productivity_types = [0.8027, 1.0, 1.2457]
transition_matrix = np.array([
    [0.7451, 0.2528, 0.0021],
    [0.1360, 0.7281, 0.1360],
    [0.0021, 0.2528, 0.7451]
])
tax_rate = 0.3

