A = []
# print(len(A))

RowNum = int(input("RowNum:"))
ColNum = int(input("ColNum"))

print("========================")
for i in range(RowNum):
  print("-Row %d ---" % i)
  A.append([])
  for j in range(ColNum):
    A[i].append(int(input("Input:")))

print("========================")
print(A)

print("========================")
for row in A:
  for a in row:
    print(a, end=" ")
  print()

print("+++++++++++++++++++++++")
print("RowNum:", len(A))
print("ColNum:", len(A[0]))

A.append([])
print("----- After A.append([]) -----")
print("RowNum:", len(A))
print("ColNum:", len(A[0]))
print("-Row %d ---" % (len(A)-1))
for j in range(len(A[0])):
  A[len(A)-1].append(int(input("Input:")))
print(A)