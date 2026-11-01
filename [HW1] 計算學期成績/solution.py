a = int(input("輸入平時成績(30%):"))
b = int(input("輸入期中成績(30%):"))
c = int(input("輸入期末成績(40%):"))

print("======================")

a_edited = a*0.3
b_edited = b*0.3
c_edited = c*0.4

print("平時:%.2f"%(a_edited))
print("期中:%.2f"%(b_edited))
print("期末:%.2f"%(c_edited))

print("----------------")

final = int(round(a_edited + b_edited + c_edited))
print(f"學期成績:{final}")