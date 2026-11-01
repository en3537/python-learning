N = int(input("N = "))

for i in range(N, 0, -1):
  for j in range(i, 0, -1):
    print(j, end="")
  print()