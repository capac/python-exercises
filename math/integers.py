m = 0
finished = False

while not finished:
    num = int(input("Enter another integer number (0 to finish): "))
    if num != 0:
        if num > m:
            m = num
    else:
        finished = True

print(str(m))
