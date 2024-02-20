Sprint 2. Итоговый проект.
---
# Создайте два калькулятора: для подсчёта денег и калорий.
---
## Вспомогательный класс  
---
```python
class Record
```
### Свойства класса
* amount - денежная сумма или количество килокалорий  
* date - передаётся в явном виде в конструктор, либо присваивается значение по умолчанию — текущая дата
* comment - комментарий, поясняющий, на что потрачены деньги или откуда взялись калории. 
## Базовый класс
---
```python
class Calculator
```
### Свойства класса
* limit - дневной лимит трат/калорий, который задал пользователь

<br>

### Методы класса
* add_record(Record) - Сохранять новую запись о расходах (приёме пищи). Принимает экземпляр класса Record(...)
* get_today_stats() - Считать, сколько денег потрачено сегодня методом
* get_week_stats() - Считать, сколько денег(каллорий) потрачено за последние 7 дней

## Классы наследники 
```python
class CaloriesCalculator #подсчет каллорий
```
### Методы класса 
* get_calories_remained() - Определяет, сколько ещё калорий можно/нужно получить сегодня
---
```python
class CashCalculator #калькулятор расходов
```
### Методы класса
* get_today_cash_remained(currency) - определяет, сколько ещё денег можно потратить сегодня в рублях, долларах или евр. Указать **'rub' или 'usd' или 'eur'**, регистр не важен



