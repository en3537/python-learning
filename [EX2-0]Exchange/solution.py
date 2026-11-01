m = int(input("m = "))
n = int(input("n = "))

if n > m:
  m, n = n, m


  '''
  a = m
  m = n
  n = a
  '''

print("============")
print("max =", m)
print("min =", n)