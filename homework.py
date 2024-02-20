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
    """Создать колькулятор с единственным принимаемым параметром - limit"""

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, obj):
        """Принимает объект класса Record(...)"""
        self.records.append((obj))

    def get_today_stats(self):
        """Считать статистику за сегодня"""
        to_day = dt.date.today()
        return sum([record.amount for record in self.records if record.date == to_day])


class Record:
    """Создаем класс записи принимает обязательные именованые аргументы
    amount и comment, date вводить необязательно"""

    def __init__(self, *, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, date_format).date()


input()
kal = Calculator(3000)
kal.add_record(Record(amount=691, comment="Катание на такси"))
kal.add_record(Record(amount=691, comment="Бегание по кругу"))
print(kal.records)
print(kal.get_today_stats())
print(type(kal.records))
