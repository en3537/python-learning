cor_id = "i001"
cor_password = "p001"

id = input("ID:")

if id != cor_id:
  print("*** ID incorrect")

else:
  password = input("PASSWORD:")

  if password != cor_password:
    print("*** PASSWORD incorrect")
  else:
    print("======================")
    score1 = int(input("請輸入國文成績:"))
    score2 = int(input("請輸入數學成績:"))
    score3 = int(input("請輸入英文成績:"))
    print("======================")

    if score1 >= 60:
        score1_grade = "及格"
    else:
        score1_grade = "不及格"

    if score2 >= 60:
        score2_grade = "及格"
    else:
        score2_grade = "不及格"

    if score3 >= 60:
        score3_grade = "及格"
    else:
        score3_grade = "不及格"

    total_score = score1 + score2 + score3

    avg_score = (score1+score2+score3)/3

    if avg_score >= 60:
      avg_grade = '及格'
    else:
      avg_grade = '不及格'

    print(f"*** 國文成績:{score1} -> {score1_grade}")
    print(f"*** 數學成績:{score2} -> {score2_grade}")
    print(f"*** 英文成績:{score3} -> {score3_grade}")


    print(f"*** 總成績:{total_score}")
    print("*** 平均成績:%.2f"%(avg_score), "->", avg_grade)