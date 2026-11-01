highScore=0
highScore_count=0

num = int(input("請輸入班級人數:"))

scores= num * [0]

for i in range(num):

    scores[i] = int(input("請輸入成績:"))

    if scores[i] > highScore:
        highScore = scores[i]
        highScore_count += 1

    elif scores == highScore:
        highScore_count += 1


print("======================")
print(f"*** 班級最高分:{highScore}")
print(f"*** 最高分人數:{highScore_count}")