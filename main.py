# import datetime
# # виклик часу

# # Створення об'єктів date і time
# date_part = datetime.date(2023, 12, 14)
# time_part = datetime.time(12, 30, 15)

# # Комбінування дати і часу в один об'єкт datetime
# combined_datetime = datetime.datetime.combine(date_part, time_part)

# print(combined_datetime)  # Виведе "2023-12-14 12:30:15"

# import datetime

# # Створення об'єкта datetime з конкретною датою
# specific_date = datetime.datetime(year=2020, month=1, day=7, hour=12, minute=35, second=59)

# print(specific_date)  # Виведе "2020-01-07 00:00:00"

# # from datetime import datetime
# # now = datetime.now()
# #  Если используешь только работу с датой-временем — удобнее from datetime import datetime, чтобы писать короче.

# #  import datetime
# # now = datetime.datetime.now()
# # Если нужно еще что-то из модуля datetime (например, типы date, time, timedelta) — тогда лучше import datetime, чтобы всё было под рукой и видно, откуда что берётся.

# from datetime import datetime

# # Створення об'єкта datetime
# now = datetime.now()

# # Отримання номера дня тижня
# day_of_week = now.weekday()

# # Поверне число від 0 (понеділок) до 6 (неділя)
# print(f"Сьогодні: {day_of_week}")

from datetime import datetime

# # Створення двох об'єктів datetime
# datetime1 = datetime(year=2023, month=3, day=14, hour=12, second=0)
# datetime2 = datetime(year=2023, month=3, day=15, hour=12, second=0)
 
#  # Порівняння дат
# print(datetime1 == datetime2)  # False, тому що дати не однакові
# print(datetime1 != datetime2)  # True, тому що дати різні
# print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
# print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2

from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=2900,
    minutes=5,
    hours=8,
    weeks=2
)
print(timedelta)