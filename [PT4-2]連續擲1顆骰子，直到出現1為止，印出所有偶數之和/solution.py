import random

count = 0
sum = 0
even_msg = ""
even_count = 0
get_one_count = 0

while True:
    num = random.randint(1, 6)
    count += 1

    if num % 2 == 0:
        sum += num
        even_count += 1
        even_msg = "-EVEN"
    else:
        even_msg = ""

    print(f"Dice {count}:{num}{even_msg}")

    if num == 1:
        get_one_count = count
        break

print("=================")
print(f"Got 1 while Dice {count}")
print(f"SUM of {even_count} EVENs = {sum}")