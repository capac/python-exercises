def getKCount(s):
    if s == 0:
        return 0
    count = 0
    for k in range(1, s+1):
        arr = []
        for i in range(k, s+1):
            arr.append(i)
            if sum(arr) == s:
                print(f'Array: {arr}, sum: {sum(arr)}')
                count += 1
                break
    return count


if __name__ == "__main__":
    s = 60
    result = getKCount(s)
    print(result)
