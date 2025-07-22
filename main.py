from pension import compute_tax_and_pension

inc, tax, pension = compute_tax_and_pension()

print("【課題2】")
print(f"中年期の期待所得：{inc:.4f}")
print(f"政府の税収合計　：{tax:.4f}")
print(f"老年期の年金額　：{pension:.4f}")

# 中年期労働所得 = productivity × 中年期の対応生産性
# 若年期生産性 p_i → 中年期生産性 p_j の確率で決まる

import numpy as np
from model import gamma, beta, r, asset_grid, productivity_types
from model import asset_grid
asset_grid = np.linspace(0, 10, 100)  # 0〜10の範囲で100点の資産グリッド
# 生産性タイプ（若年期）：低・中・高
productivity_types = [0.8027, 1.0, 1.2457]

# 遷移確率行列 P（若年→中年）
transition_matrix = np.array([
    [0.7451, 0.2528, 0.0021],
    [0.1360, 0.7281, 0.1360],
    [0.0021, 0.2528, 0.7451]
])

# 税率
tax_rate = 0.3

# 利子率
r = 1.02520** - 1

#ガンマ
gamma = 2.0


# 全タイプに対する中年期の平均労働所得
average_income_mid = sum(
    (1/3) * sum(transition_matrix[i, j] * productivity_types[j] for j in range(3))
    for i in range(3)
)

# 税収（中年期人口は1/3 × 3 = 1）
total_tax_revenue = tax_rate * average_income_mid

# 年金額（利子率で運用し老年期に分配、受給者も1人）
pension = (1 + r) * total_tax_revenue

def utility(c):
    return (c**(1 - gamma)) / (1 - gamma) if c > 0 else -1e10

def solve_lifecycle(pension_given=True):
    policy = np.zeros((3, len(asset_grid)))
    for z, prod in enumerate(productivity_types):
        V3 = np.array([utility(a*(1 + r) + (pension if pension_given else 0)) for a in asset_grid])
        policy3 = np.zeros_like(V3)

        V2 = np.zeros_like(asset_grid)
        policy2 = np.zeros_like(asset_grid)

        for i, a in enumerate(asset_grid):
            income2 = prod
            budget = (1 + r)*a + income2*(1 - tax_rate)
            max_val = -np.inf
            for j, a_next in enumerate(asset_grid):
                c = budget - a_next
                if c <= 0:
                    continue
                val = utility(c) + beta * V3[j]
                if val > max_val:
                    max_val = val
                    policy2[i] = a_next
            V2[i] = max_val

        V1 = np.zeros_like(asset_grid)
        policy1 = np.zeros_like(asset_grid)

        for i, a in enumerate(asset_grid):
            income1 = prod
            budget = (1 + r)*a + income1
            max_val = -np.inf
            for j, a_next in enumerate(asset_grid):
                c = budget - a_next
                if c <= 0:
                    continue
                val = utility(c) + beta * V2[j]
                if val > max_val:
                    max_val = val
                    policy1[i] = a_next
            V1[i] = max_val

        policy[z, :] = policy1  # 若年期の政策関数

    return policy

import matplotlib.pyplot as plt

policy_no_pension = solve_lifecycle(pension_given=False)
policy_with_pension = solve_lifecycle(pension_given=True)

fig, ax = plt.subplots()
for i, label in enumerate(['Low', 'Middle', 'High']):
    ax.plot(asset_grid, policy_no_pension[i], label=f'{label} - No Pension', linestyle='--')
    ax.plot(asset_grid, policy_with_pension[i], label=f'{label} - With Pension')

ax.set_xlabel("資産（期初、若年期）")
ax.set_ylabel("次期資産（若年期末）")
ax.set_title("政策関数の比較（年金導入前後）")
ax.legend()
plt.grid()
plt.show()
