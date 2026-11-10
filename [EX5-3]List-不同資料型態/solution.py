a = [0, 3.5]
print(a)

print("================")

a.append('ABC')
print(a)

print("================")

for i in range(len(a)):
  print("a[%d]="% i, a[i])

  # print("a[%d]=%d"% (i, a[i]))
  # TypeError: %d format: a real number is required, not str