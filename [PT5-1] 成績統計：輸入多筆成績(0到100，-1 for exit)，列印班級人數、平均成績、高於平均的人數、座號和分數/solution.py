print("請輸入成績(-1 for exit)")

scores=[]
avg_score=0
abv_avg=0


while True:
  score = int(input(f"No.{len(scores)+1}:"))

  if score == -1:
    break
  elif score > 100 or score < 0:
    print("*** Error Data!")
  else:
    scores.append(score)

print("=============================")
print(f"班級人數:{len(scores)}")

if len(scores) > 0:
  avg_score = (sum(scores)/len(scores))
  print("平均成績:%.2f"% avg_score)
  print("===========高於平均==========")

  for i in range(len(scores)):
    if scores[i] > avg_score:
      abv_avg+=1
      print(f"No.{i+1}:{scores[i]}")

  if abv_avg > 0:
    print("-------------")

  print(f"共有 {abv_avg} 人")