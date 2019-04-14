def time_f(time):
    hours, minutes = time[:-2], time[-2:]
    if divmod(int(hours), 12)[0] >= 2:
        print("Hours must be between 0 and 23!")
        return False
    if divmod(int(minutes), 60)[0] >= 1:
        print("Minutes must be between 0 and 59!")
        return False
    return True


def am_pm(time):
    hours, minutes = time[:-2], time[-2:]
    if divmod(int(hours), 12)[0] < 1:
        return f'{hours}:{minutes} am'
    elif divmod(int(hours), 12)[0] >= 1 and divmod(int(hours), 12)[0] < 2:
        return f'{str(int(hours) - 12)}:{minutes} pm'


if __name__ == "__main__":
    time = input("Enter a number between 0 and 2359 to represent the time: ")
    if time_f(time):
        hours = int(time[:-2])
        if hours > 0 and hours <= 4:
            print(f"It's {am_pm(time)}, you should be sleeping!")

        elif hours > 4 and hours < 12:
            print(f"It's {am_pm(time)}, good morning!")

        elif hours > 12 and hours <= 17:
            print(f"It's {am_pm(time)}, good afternoon!")

        elif hours > 17 and hours <= 22:
            print(f"It's {am_pm(time)}, good evening!")

        elif hours > 22 and hours < 24:
            print(f"It's {am_pm(time)}, good night!")
        else:
            print(f"{am_pm(time)}")
