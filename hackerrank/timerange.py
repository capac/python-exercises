class TimeRange():
    '''Represents a time range (the time between a start time and an end time)
    Example usage:
        >>> time_range = TimeRange('3-5')
        >>> print(time_range.start)
        3.0
        >>> print(time_range.end)
        5.0
        >>> print(time_range.end - time_range.start)
        2.0
    '''

    def __init__(self, range_string):
        # for example, convert "3-5" into start=3.0 and end=5.0
        self.start, self.end = [
            float(time)
            for time in range_string.split('-')
        ]

    def open_hours_ratio(query_time_range, open_hours):
        time_range = query_time_range.end - query_time_range.start
        return time_range/sum([hour.end - hour.start for hour in open_hours])


if __name__ == "__main__":
    # input handling
    line = input('Enter time intervals: ')
    input_line_1 = ''.join([line.split(',')[0]])
    input_line_2 = ', '.join([item.strip() for item in line.split(',')[1:]])
    query_time_range = TimeRange(input_line_1)
    if input_line_2:
        # for example, convert "1-3, 5-7" into [(1, 3), (5, 7)]
        open_hours = [
            TimeRange(range_string)
            for range_string in input_line_2.split(', ')
        ]
    else:
        # if the input string is empty, then the business is never open
        open_hours = []

    # compute answer and display to 2 decimal places
    ratio = TimeRange.open_hours_ratio(query_time_range, open_hours)
    print('{:.2f}'.format(ratio))
