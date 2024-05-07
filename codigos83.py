
import calendar

# print(calendar.calendar(2022))
# print(calendar.month(2022, 8))

numero_primeiro_dia, ultimo_dia = calendar.monthrange(2022,12)
# print(list(enumerate(calendar.day_name)))
# print(calendar.day_name[numero_primeiro_dia])
# print(calendar.day_name[calendar.weekday(2022,12, ultimo_dia)])

for week in calendar.monthcalendar(2022,12):
    for day in week:
        if day ==0:
            continue
        print(day)