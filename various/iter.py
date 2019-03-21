class Range:
    # home-built Range function
    def __init__(self, start, end):
        # init our Range function it's a special method
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        # this declares this object as an iterable
        return self

    def __next__(self):
        # this return the next item in the iteration
        if self.current >= self.start and self.current < self.end:
            val = self.current
            self.current += 2
            return val
        else:
            raise StopIteration


# this is for the loop
for i in Range(0, 20):
    print(i)
