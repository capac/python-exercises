import datetime


def str_to_date(dt):
    return datetime.datetime.strptime(dt, '%Y%m%d%H%M%S')


def compute_dd(bday1, bday2):
    diff_bdays = abs(str_to_date(bday1) - str_to_date(bday2))
    dd = diff_bdays + str_to_date(max(bday1, bday2))
    return str(dd)


if __name__ == "__main__":
    d1 = input("Enter first birthday: ")
    d2 = input("Enter second birthday: ")
    print("Double day is: ", compute_dd(d1, d2))
