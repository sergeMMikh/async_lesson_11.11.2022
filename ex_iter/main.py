import datetime


class DateRange:

    def __init__(self, start: datetime.date, end: datetime.date, step_days: int = 1):
        self.start = start
        self.end = end
        self.step = datetime.timedelta(days=step_days)

    def __iter__(self):
        self.cursor = self.start
        return self

    def __next__(self):
        self.cursor += self.step
        if self.cursor >= self.end:
            raise StopIteration

        return self.cursor


for item in DateRange(datetime.date(2022, 1, 1),
                      datetime.date(2022, 1, 10),
                      1):
    print(item)
