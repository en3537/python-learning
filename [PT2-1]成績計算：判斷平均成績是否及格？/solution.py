score1 = int(input("請輸入國文成績:"))
score2 = int(input("請輸入數學成績:"))
score3 = int(input("請輸入英文成績:"))

total_score = score1 + score2 + score3

avg_score = (score1+score2+score3)/3

if avg_score >= 60:
  grade = '及格'
else:
  grade = '不及格'

print("======================")
print(f"*** 總成績:{total_score}")
print("*** 平均成績:%.2f"%(avg_score), "->", grade)