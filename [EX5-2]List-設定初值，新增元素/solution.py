a = [0, 0, 0]

print(a)

a.append(10)

print(a)

print("===============")

b = [0 for i in range(3)]

for i in range(3):
  print("b[%d]=%d"% (i, b[i]))

print("===============")

c = [i for i in range(3)]

for i in range(len(c)):
  print("c[%d]=%d"% (i, c[i]))

print("===============")

#############
for k in c:
  print(k)
#############