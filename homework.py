import datetime as dt

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

        to_day = dt.date.today()
        date_week_ago = to_day - dt.timedelta(days=7)
        return sum(
            [
                record.amount
                for record in self.records
                if date_week_ago < record.date <= to_day
            ]
        )

    def get_today_remained(self):

        return self.limit - self.get_today_stats()


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


class CaloriesCalculator(Calculator):
    """Калькулятор каллорий, метод дополняющий родительского класс Calculator
    это get_today_calories_remained"""

    def get_calories_remained(self):
        some = self.get_today_remained()
        if some > 0:
            return "Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {} кКал".format(
                some
            )
        else:
            return "Хватит есть!"


class CashCalculator(Calculator):
    """Калькулятор каллорий, метод метод отличный от родительского класса Calculator это get_today_cash_remained"""

    USD_RATE = 82.0
    EURO_RATE = 95.0
    RUB_RATE = 1.0

    def get_today_cash_remained(self, cur="rub"):
        # currency = dict(rub=self.RUB_RATE, eur=self.EURO_RATE, usd=self.USD_RATE)
        currency = {
            "rub": ("руб", self.RUB_RATE),
            "eur": ("Euro", self.EURO_RATE),
            "usd": ("USD", self.USD_RATE),
        }
        if cur.lower() not in currency:
            raise ValueError("Валюта введена НЕ ВЕРНО")
        name_cur, rate = currency[cur.lower()]
        ballance = self.get_today_remained()
        currency_ballance = abs(round(ballance / rate, 2))
        if ballance == 0:
            return "Денег нет, держись"
        elif ballance > 0:
            return f"На сегодня осталось {currency_ballance} {name_cur}"

        return f"Денег нет, держись: твой долг - {currency_ballance} {name_cur}"


fff = CashCalculator(1000)
fff.add_record(Record(amount=145, comment="кофе"))
fff.add_record(Record(amount=2145, comment="чай"))
print(fff.get_today_cash_remained("eur"))
