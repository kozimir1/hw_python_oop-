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
    """Создать колькулятор с единственным принимаемым параметром - limit
    методы add_record,get_today_stats,get_week_stats"""

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

    def get_week_stats(self):
        """Статистика за неделю"""

        one_week = dt.date.today() - dt.timedelta(7)
        return sum([record.amount for record in self.records if record.date > one_week])


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


# class CaloriesCalculator(Calculator):
# 	if some>0:
# 		retturn

input()
kal = Calculator(3000)
kal.add_record(Record(amount=691, comment="Катание на такси"))
kal.add_record(Record(amount=691, comment="Бегание по кругу"))
kal.add_record(Record(amount=123, comment="Вонючесть", date="14.02.2024"))
print(kal.records)
print(kal.get_today_stats())
print(kal.get_week_stats())
print(type(kal.records))
