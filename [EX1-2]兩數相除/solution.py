a = int(input("a = "))
b = int(input("b = "))
print("整數a=%d，整數b=%d，a除以b的餘數是%d"%(a, b, a%b))
print("整數a={}，整數b={}，a除以b的餘數是{}".format(a, b, a%b))
print(f"整數a={a}，整數b={b}，a除以b的餘數是{a%b}")
print("整數a=", a, "整數b=", b, "a除以b的餘數是", a%b)


print("a / b =", a/b)
print("a / b = %.2f"%(a/b)) # 2位小數，四捨五入
print("a / b =", round(a/b, 1)) # 四捨五入，1位小數
print("a // b =", a//b) # 商數