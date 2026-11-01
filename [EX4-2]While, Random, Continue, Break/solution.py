import random
while True:
  a = random.randint(0, 9)
  print(a, end = "")
  if a==0:
    break
  if a % 2 == 0:
    print()
    continue
  print(" : odd")
print(" : stop")