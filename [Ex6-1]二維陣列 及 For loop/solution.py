A = [
  [40, 50],
  [60, 90],
  [90, 70],
  [40, 10]
]

print("==========(1)==========")
print(A)

print("==========(2)==========")
for i in range(4):
  for j in range(2):
    print(A[i][j], end=" ")
  print()

print("==========(3)==========")
for i in range(len(A)):
  for j in range(len(A[0])):
    print(A[i][j], end=" ")
  print()

print("==========(4)==========")
for row in A:
  print(row)

print("==========(5)==========")
for row in A:
  for a in row:
    print(a, end=" ")
  print()