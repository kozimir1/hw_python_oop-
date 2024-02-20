import datetime as dt

datetime_str = "25.12.2022 23:20:59"


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

    def add_record(self, obj):
        self.records.append((obj.amount, obj.date, obj.comment))


class Record:
    """Создаем класс записи"""

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, date_format).date()


input()
kal = Calculator(3000)
kal.add_record(Record(amount=691, comment="Катание на такси", date="08.03.2022"))
print(kal.records)
print(type(kal.records))
