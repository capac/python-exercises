def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


class Time():
    def __init__(self, hr=0, mnt=0, sec=0):
        self.hour = hr
        self.minute = mnt
        self.second = sec

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        elif isinstance(other, int):
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return '%.2dh %.2dm %.2ds' % (self.hour, self.minute, self.second)

    def time_to_int(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '%s, %s' % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        elif isinstance(other, tuple):
            return self.add_tuple(other)
        else:
            msg = "Point doesn't know how to add type " + str(type(other))
            raise TypeError(msg)

    def __radd__(self, other):
        return self.__add__(other)

    def add_point(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def add_tuple(self, other):
        return Point(self.x + other[0], self.y + other[1])


def main():
    start = Time(2, 24, 55)
    duration = Time(3, 15, 34)
    seconds = 13436
    add_time = start.increment(seconds)
    pt_1 = Point(7, 8)
    pt_2 = Point(4, 6)
    pt_3 = Point(5, 2)
    pt_4 = (5, 3)
    print('Start:', start)
    print('Duration:', duration)
    print('Start time to seconds:', start.time_to_int())
    # f-string literal formatting
    print(f'Adding {seconds!a} seconds to {start!s} gives {add_time!s}')
    print(f'Start + duration: {start + duration}')
    print(f'Point 1 ({pt_1}) and point 2 ({pt_2}) equals ({pt_1 + pt_2})')
    print(f'Tuple {pt_4} and point 2 ({pt_2}) equals ({pt_4 + pt_2})')
    print(f'Sum of time {duration} and {start} is {sum([duration, start])}')
    print(
        f'Sum of points ({pt_1!s}), ({pt_2!s}), ({pt_3!s}) is ({pt_1+ pt_2+pt_3!s})')
    print(f'vars(start): {vars(start)}')


if __name__ == "__main__":
    main()
