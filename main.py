from pension import compute_tax_and_pension

inc, tax, pension = compute_tax_and_pension()

print("【課題2】")
print(f"中年期の期待所得：{inc:.4f}")
print(f"政府の税収合計　：{tax:.4f}")
print(f"老年期の年金額　：{pension:.4f}")
