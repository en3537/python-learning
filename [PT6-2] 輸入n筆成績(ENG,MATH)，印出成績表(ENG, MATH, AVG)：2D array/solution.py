s = int(input("請輸入班級人數="))

g = [[0.0 for i in range(3)] for j in range(s)]
a = ["ENG", "MATH", "AVG"]

avg=0

for i in range(1, s+1):
    print("===== No.%d ====="% i)
    g[i-1][0] = int(input("ENG:"))
    g[i-1][1] = int(input("MATH:"))
    g[i-1][2] = float((g[i-1][0] + g[i-1][1]) / 2)

print("")
print("====NO.===%s====%s====%s====" % (a[0], a[1], a[2]))

for z in range(1, len(g)+1):
    print("     %d     %d     %d     %.1f" % (z, g[z-1][0], g[z-1][1], g[z-1][2]))

print("================================")