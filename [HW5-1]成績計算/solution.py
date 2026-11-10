scores=[]
lower_score=[0]
min_count=0
message=""


size = int(input("請輸入班級人數:"))

while True:
    score = int(input(f"{len(scores)+1}號成績:"))

    if score > 100 or score < 0:
        continue
    else:
        scores.append(score)

        if len(scores) == 1 or score < lower_score[0]:
            lower_score[0] = score

    if len(scores) == size:
        break

print(f"===== 最低分:{lower_score[0]} =====")

for i in range(len(scores)):
    if scores[i] == lower_score[0]:
        min_count+=1
        print(f"*** {i+1}號")

print("--------------------")
print(f"+++ 共{min_count}人")

print("")
print("========== 查詢分數 ===========")

while True:
    stuNo = int(input("請輸入座號(-1 for exit):"))

    if stuNo == -1:
        print("=== BYE ===")
        break

    if stuNo > len(scores):
        print("+++ Error: 座號錯誤")
    else:
        if scores[stuNo-1] == lower_score[0]:
            message = " <--- 最低分"

        print(f"*** {stuNo}號:{scores[stuNo-1]}分{message}")

    print("--------------------")