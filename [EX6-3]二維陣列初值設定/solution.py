# 錯誤
a = [[0]*5]*5
print(a)

print("============")
a[1][2] = 3
for i in range(5):
  for j in range(5):
    print(a[i][j], end=" ")
  print()

# ===================================
print("============")
# a = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
a = [[0 for i in range(5)] for j in range(5)]

a[1][2] = 3
for i in range(5):
  for j in range(5):
    print(a[i][j], end=" ")
  print()