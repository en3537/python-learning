counter=0
message="NO"

n = int(input("n="))

map=[[0 for i in range(n)] for j in range(n)]

print("=============")

while True:
    if counter == n:
        break

    inxy = input("x,y:")

    xy = inxy.split(",")

    x = int(xy[0])
    y = int(xy[1])


    if x < 1 or y < 1 or x > n or y > n:
        print("*** Error")
        continue
    else:
        counter+=1
        map[x-1][y-1]=1

print("=============")

for a in range(len(map)):
    for b in range(len(map)):
        print(map[a][b], end=" ")
    print()

print("=============")


# 直線
for a in range(n):
    count=0
    for b in range(n):
        if map[b][a] == 1:
            count+=1

    if count == n:
        message="YES"
        # message="直線"


# 橫線
for c in range(n):
    count=0
    for d in range(n):
        if map[c][d] == 1:
            count+=1

    if count == n:
        message="YES"
        # message="橫線"

print(f"*** {message}")