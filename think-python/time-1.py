def int_to_time(seconds):
    time = Time()
    minutes, time.sec = divmod(seconds, 60)
    hours, time.min = divmod(minutes, 60)
    time.dy, time.hr = divmod(hours, 24)
    return time


def avg_pace(time, num):
    return int_to_time(round(time.time_to_int()/num))


class Time:
    def __init__(self, day=0, hour=0, minute=0, second=0):
        self.dy = day
        self.hr = hour
        self.min = minute
        self.sec = second
    def __str__(self):
        return "{0:02d}d {1:02d}h {2:02d}m {3:02d}s".format(self.dy, self.hr, self.min, self.sec)
    def time_to_int(self):
        return self.dy*24*60*60 + self.hr*60*60 + self.min*60 + self.sec
    def __add__(self, other):
        return int_to_time(self.time_to_int() + other.time_to_int())

if __name__ == "__main__":
    time1 = Time(0, 1, 9, 34)
    print("Time1: ", time1)
    print("Time1 in seconds: {}s".format(time1.time_to_int()))
    dist1=14.3
    print("Time1: {0}, distance: {1}, pace: {2}".format(time1, dist1, avg_pace(time1, dist1)))
    time2 = Time(0, 0, 23, 29)
    print("Time2: ", time2)
    dist2=5.0
    print("Time2 in seconds: {}s".format(time2.time_to_int()))
    print("Time2: {0}, distance: {1}, pace: {2}".format(time2, dist2, avg_pace(time2, dist2)))
    print("Sum of time1 and time2: ", time1 + time2)
