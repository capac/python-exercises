#! /usr/bin/env python3


def dayOfProgrammer(year):
    year = int(year)
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    prog_day = 256
    # Gregorian calendar
    if year > 1918 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        months[1] += 1
    # Jump from Julian to Gregorian
    elif year == 1918:
        months[1] = 15
    # Julian calendar
    elif year < 1918 and year % 4 == 0:
        months[1] += 1
    cumul_months = []
    count_days = 0
    for days in months:
        count_days += days
        cumul_months.append(count_days)
    for counter, days in enumerate(cumul_months):
        diff = days - prog_day
        if diff > 0:
            month = months[counter]
            month -= diff
            break
    result = f'{str(month).zfill(2)}.{str(counter+1).zfill(2)}.{str(year)}'
    return result


if __name__ == '__main__':
    year = input('Please provide a year: ')
    result = dayOfProgrammer(year)
    print(result)
