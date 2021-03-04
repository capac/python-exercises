#! /usr/bin/env python


# from itertools import combinations


# def non_divisible_subset(s, k):
#     arr = []
#     # print(f'List: {list(combinations(s, 2))}')
#     # print(f'Length list: {len(list(combinations(s, 2)))}')
#     for comb in list(combinations(s, 2)):
#         if sum(comb) % k != 0:
#             # print(f'Combinations: {combinations}')
#             arr.append(comb)
#     res = set(item for pair in arr for item in pair)
#     print(f'Result: {res}')
#     return len(res)


def non_divisible_subset(s, k):
    cnt = [0] * k
    for x in s:
        cnt[x % k] += 1
    print(f'Cnt: {cnt}')
    ans = min(cnt[0], 1)
    for rem in range(1, (k + 1) // 2):
        ans += max(cnt[rem], cnt[k - rem])
        print(f'Ans: {ans}')
    if k % 2 == 0:
        ans += min(cnt[k // 2], 1)
        print(f'Ans % 2: {ans}')
    return ans


if __name__ == "__main__":
    # s = [int(s) for s in list(input('Please input array as string: '))]
    # k = int(input('Please input non-factor: '))
    # s = sorted([278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436])
    s = sorted([422346306, 940894801, 696810740, 862741861, 85835055, 313720373], reverse=False)
    # k = 7
    k = 8
    res = non_divisible_subset(s, k)
    print(f'Results: {res}')
