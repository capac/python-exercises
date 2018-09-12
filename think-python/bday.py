import datetime


def days_to_next_bday(date):
    today = datetime.datetime.today()
    date_bday = datetime.datetime.strptime(date, "%Y%m%d%H%M%S")
    bday = datetime.datetime(today.year, date_bday.month, date_bday.day,
                             date_bday.hour, date_bday.minute, date_bday.second)
    if today > bday:
        next_bday = bday.replace(year=today.year + 1)
        time_until_next_bday = next_bday - today
    else:
        time_until_next_bday = bday - today
    days = str(time_until_next_bday).split(' ')[0]
    hms = str(time_until_next_bday).split(' ')[2].split(':')
    return "{0:s} days, {1:s} hours, {2:s} minutes, {3:d} seconds".format(days, hms[0], hms[1], round(float(hms[2])))


def main():
    date_str = input(
        "Enter birthday as year, month, day, hours, minutes and seconds: ")
    print("Time until next birthday: ", days_to_next_bday(date_str))


if __name__ == "__main__":
    main()
