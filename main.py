import matplotlib.pyplot as plt
from model import asset_grid
from policy import solve_savings_policy, productivity_types
from scipy.optimize import minimize_scalar

# 政策関数計算
policy_functions = solve_savings_policy(asset_grid)

# 描画
plt.figure(figsize=(8,6))
labels = ['低生産性', '中生産性', '高生産性']
for i in range(3):
    plt.plot(asset_grid, policy_functions[i], label=labels[i])
    
plt.xlabel('若年期期初の資産（利子除く）')
plt.ylabel('中年期期初の資産（利子除く）')
plt.title('貯蓄政策関数（年金なし）')
plt.legend()
plt.grid()
plt.savefig('output/figures/policy_function_no_pension.png')
plt.show()
