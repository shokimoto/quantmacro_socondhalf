import numpy as np
from scipy.optimize import minimize_scalar
from model import gamma, beta, r, asset_grid, productivity_types

def utility(c):
    if c <= 0:
        return -1e10  # 非現実的な消費は極端にペナルティ
    else:
        return (c ** (1 - gamma)) / (1 - gamma)

def solve_savings_policy(w):
    policy = []
    for y in productivity_types:
        a_prime_list = []
        for a in asset_grid:
            def objective(a_prime):
                c = y + (1 + r) * a - a_prime
                return -utility(c)  # 最大化したいのでマイナス

            result = minimize_scalar(objective, bounds=(0, y + (1 + r) * a), method='bounded')
            a_prime_list.append(result.x)

        policy.append(a_prime_list)
    return np.array(policy)
