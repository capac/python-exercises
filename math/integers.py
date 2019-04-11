m = 0
finished = False

while not finished:
    print("Enter another integer number (0 to finish): ", end="")
    num = int(input())
    if num != 0:
        if num > m:
            m = num
    else:
        finished = True
print(str(m))
