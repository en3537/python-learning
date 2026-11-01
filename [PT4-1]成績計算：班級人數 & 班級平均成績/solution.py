count = 0
sum_scores = 0

while True:
  scores = int(input("請輸入成績:(-1 for exit)"))

  if scores == -1:
    break

  if scores > 100 or scores < 0:
    print("*** Error Data!")
    continue

  sum_scores += scores
  count += 1

print("======================")

if count == 0:
    print("班級人數:%d" % count)

else:
    avg_score = sum_scores / count
    print("班級人數:%d" % count)
    print("平均成績:%.2f" % avg_score)