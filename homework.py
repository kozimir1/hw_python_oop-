import datetime as dt

datetime_str = "25.12.2022 23:20:59"

my_datetime = dt.datetime.strptime(datetime_str, "%H:%M:%S %d.%m.%Y")

print(my_datetime)

fff = dt.date(1992, 10, 6)

print(dt.date.today().isoweekday())
print(fff)
print(dt.date.toordinal(fff))
print(type(fff))

ttt = dt.time(11, 26)
print(ttt)
print(type(ttt))
print(*[ttt, fff])

date_format = "%d.%m.%Y"


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []


class Record:
    """Создаем класс записи"""

    def __init__(self, *, amount, comment, date=None):
        self.amount = amount
        self.date = date
        self.comment = comment
        if date is None:
            self.date = dt.datetime(date, date_format).date()
        else:
            self.date = dt.date.today()
