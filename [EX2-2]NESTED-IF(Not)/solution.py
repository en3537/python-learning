print("輸入學生成績，將會輸出對應的成績級別")
score = int(input("輸入成績(0-100):"))
if score >= 80 and score <= 100:
  grade = 'A'
if score >= 60 and score <= 79:
  grade = 'B'
if score >= 0 and score <=59:
  grade = 'C'
print("此成績級別為", grade)