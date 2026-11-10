x = [10, 20, 30]
print("==========(1)==========")
print(x)
print("---------------")
for b in x:
  b=0
print(x)

A = [[40, 50], [60, 90], [90, 70], [40, 10]]
print("==========(2)==========")
for row in A:
  for a in row:
    a=0
for row in A:
  for a in row:
    print(a, end=" ")
  print()

print("==========(3)==========")
print(A)
for i in range(len(A)):
  for j in range(len(A[0])):
    A[i][j]=0
print(A)