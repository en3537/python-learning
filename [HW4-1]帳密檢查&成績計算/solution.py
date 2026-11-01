# 帳密檢查
chance=3
acc_id="i001"
acc_pwd="p001"

# 成績
scores=[]
cz=0
count=0
sum=0
pass_count=0
highScore=0
highScore_count=0


for i in range(0, chance):
    print("================================")

    input_id = input("ID=")
    input_pwd = input("PASSWORD=")

    chance-=1

    if input_id == acc_id and input_pwd == acc_pwd:
        print("================================")

        while True:
            score = int(input("請輸入成績:(-1 for exit)"))

            if score == -1:
                break

            if score > 100 or score < 0:
                print("*** Error Data!")
                continue

            scores.append(score)

            if score >= 60:
                pass_count+=1

            if score > highScore:
                highScore = score
                highScore_count = 1
            elif score == highScore:
                highScore_count += 1

            cz += 1
            count += 1
            sum += score

        avg_score = (sum/count)

        print("================================")
        print("班級人數:%d"% count)
        print("及格人數:%d"% pass_count)
        print("最高分:%d"% highScore)
        print("最高分人數:%d"% highScore_count)
        print("平均成績:%.2f"% avg_score)
        break

    elif chance == 0:
        print("*** Sign-in failed.")
        print("*** User login: failed 3 times")
        break
    else:
        print("*** Sign-in failed.")
        print(f"*** You have {chance} more chance(s)!")
        continue