import numpy as np
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# パラメータ・グリッド
beta = 0.98520
gamma = 2.0
r = 1.02520 - 1
tax_rate = 0.3
asset_grid = np.linspace(0, 10, 100)
productivity_types = [0.8027, 1.0, 1.2457]
P = np.array([
    [0.7451, 0.2528, 0.0021],
    [0.1360, 0.7281, 0.1360],
    [0.0021, 0.2528, 0.7451]
])

# 年金額の計算
avg_income = sum((1/3) * sum(P[i,j] * productivity_types[j] for j in range(3)) for i in range(3))
total_tax = tax_rate * avg_income
pension = (1 + r) * total_tax

def utility(c):
    return (c**(1 - gamma)) / (1 - gamma) if c > 0 else -1e10

def expected_lifetime_utility(pension_given=True):
    utilities = []
    for z, prod_young in enumerate(productivity_types):
        probs = P[z]
        total = 0
        for z2, prob in enumerate(probs):
            prod_mid = productivity_types[z2]
            best = -np.inf
            for a2 in asset_grid:
                c1 = prod_young - a2
                if c1 <= 0: continue
                for a3 in asset_grid:
                    c2 = (1 + r)*a2 + prod_mid*(1 - tax_rate) - a3
                    if c2 <= 0: continue
                    c3 = (1 + r)*a3 + (pension if pension_given else 0)
                    if c3 <= 0: continue
                    u = utility(c1) + beta * utility(c2) + beta**2 * utility(c3)
                    best = max(best, u)
            total += prob * best
        utilities.append(total)
    return sum(utilities) / 3

# 実行
u0 = expected_lifetime_utility(pension_given=False)
u1 = expected_lifetime_utility(pension_given=True)

print(f"年金なし: {u0:.4f}")
print(f"年金あり: {u1:.4f}")
print("増加" if u1 > u0 else "減少")
