import numpy as np
from model import productivity_types, P, r

def compute_tax_and_pension(tax_rate=0.3):
    """
    中年期の税収と老年期の年金額を計算
    """
    # 若年期タイプごとの確率
    prob = 1/3
    expected_middle_income = 0.0

    for i, y_young in enumerate(productivity_types):
        for j, y_middle in enumerate(productivity_types):
            expected_middle_income += prob * P[i][j] * y_middle

    # 総税収（人口1なので合計）
    tax_total = tax_rate * expected_middle_income

    # 政府が利子率rで運用
    fund = tax_total * (1 + r)

    # 人口1に対して均等給付（全員に同額）
    pension = fund

    return expected_middle_income, tax_total, pension
