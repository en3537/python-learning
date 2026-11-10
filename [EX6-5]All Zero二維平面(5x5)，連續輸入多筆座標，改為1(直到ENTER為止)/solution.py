a = [[0 for i in range(5)] for j in range(5)]
for i in range(5):
  for j in range(5):
    print(a[i][j], end=" ")
  print()

print("")
print("============")
print("")

while True:
  inxy = input('x,y:')
  if inxy == '':
    break
  xy = inxy.split(',')
  print(xy)
  x = int(xy[0])
  y = int(xy[1])
  a[x][y] = 1

print("")
print("============")
print("")

for i in range(5):
  for j in range(5):
    print(a[i][j], end=" ")
  print()