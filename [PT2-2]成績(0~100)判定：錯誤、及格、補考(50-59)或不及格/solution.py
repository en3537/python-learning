score = int(input("請輸入成績:"))

print("======================")
if score <= 100 and score >= 60:
    grade="及格"
    print(f"+++ 成績:{score} -> {grade}")
elif score < 60 and score >= 50:
    grade="補考"
    print(f"+++ 成績:{score} -> {grade}")
elif score < 50 and score >= 0:
    grade="不及格"
    print(f"+++ 成績:{score} -> {grade}")
else:
    grade="成績錯誤"
    print(f"*** {grade}")