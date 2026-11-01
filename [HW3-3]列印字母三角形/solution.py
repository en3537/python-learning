N = int(input("N = "))

for i in range(N, 0, -1):
  for j in range(i, 0, -1):
    print(chr(ord('A')+j-1), end="")
  print()