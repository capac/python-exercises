#! /usr/bin/env python3

import os

# Complete the timeConversion function below.


def timeConversion(s):
    am_pm_suffix = s[-2:]
    hms_list = s[:-2].split(':')
    if am_pm_suffix == 'PM' and int(hms_list[0]) >= 1 and int(hms_list[0]) <= 11:
        hms_list[0] = str(int(hms_list[0])+12)
        if int(hms_list[0]) == 24:
            hms_list[0] = '00'
    elif am_pm_suffix == 'AM' and int(hms_list[0]) == 12:
        hms_list[0] = '00'
    return f'{hms_list[0]}:{hms_list[1]}:{hms_list[2]}'


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    f.write(result + '\n')
    f.close()
