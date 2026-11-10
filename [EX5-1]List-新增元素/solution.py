a = []
# a[0] = 10
a.append(10)
print(a)
print(a[0])

print("================")

for i in range(10):
  a.append(0)
print(a)

print("================")

for i in range(10):
  print("a[%d]=%d"% (i, a[i]) )

print("================")

print("a[%d]=%d"% (10, a[10]) )

print("================================")

print("# of elements in list a = ", len(a))

for i in range(len(a)):
  print("a[%d]=%d"% (i, a[i]) )

# print("a[%d]=%d"% (11, a[11]) )