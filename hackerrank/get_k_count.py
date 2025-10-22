def getKCount(s):
    if s == 0:
        return 0
    count = 0
    for k in range(1, s+1):
        sum_ = 0
        tmp_list = []
        for i in range(k, s+1):
            tmp_list.append(i)
            sum_ += i
            if sum_ == s:
                print(f'Array: {tmp_list}, sum: {sum(tmp_list)}')
                count += 1
                tmp_list = []
    return count


if __name__ == "__main__":
    s = 30
    result = getKCount(s)
    print(result)
