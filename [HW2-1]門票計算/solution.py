print("====== 票價計算 ======")

age = int(input("*** 年齡:"))

fee = 100
final_fee= 0

if (age >= 7 and age <= 12) or (age >= 50 and age <=79):
  final_fee = fee // 2

elif age < 7 or age >= 80:
  final_fee = 0

else:
  final_fee = 100

print(f"+++ Fee:{final_fee}")