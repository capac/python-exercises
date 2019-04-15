
class Greet():
    def __init__(self, time):
        self.time = time

    def time_check(self):
        hours, minutes = self.time[:-2], self.time[-2:]
        if divmod(int(hours), 12)[0] >= 2:
            print("Hours must be between 0 and 23!")
            return False
        if divmod(int(minutes), 60)[0] >= 1:
            print("Minutes must be between 0 and 59!")
            return False
        return True

    def time_format(self):
        hours, minutes = self.time[:-2], self.time[-2:]
        am_pm = 'am' if int(hours) < 12 else 'pm'
        hours = int(hours) % 12 if int(hours) % 12 != 0 else 12
        return f'{str(hours)}:{minutes} {am_pm}'


if __name__ == "__main__":
    time = input("Enter a number between 0 and 2359 to represent the time: ")
    greetings = Greet(time)
    if greetings.time_check():
        hours = int(time[:-2])
        if hours >= 0 and hours < 4:
            print(f"It's {greetings.time_format()}, you should be sleeping!")

        elif hours >= 4 and hours < 12:
            print(f"It's {greetings.time_format()}, good morning!")

        elif hours >= 12 and hours < 17:
            print(f"It's {greetings.time_format()}, good afternoon!")

        elif hours >= 17 and hours < 22:
            print(f"It's {greetings.time_format()}, good evening!")

        elif hours >= 22 and hours < 24:
            print(f"It's {greetings.time_format()}, good night!")
        else:
            print(f"{greetings.time_format()}")
