n = int(input("n = "))

print("-------------------------")
a = ord('a')
print("'a' 的 ASCII code:", a)

c = chr(a + n - 1)
print("第%d個小寫英文字母: %c"%(n, c))

print("-------------------------")
print("'A' 的 ASCII code:", ord('A'))
print("第%d個小寫英文字母: %c"%(n, chr(ord('A')+n-1)))