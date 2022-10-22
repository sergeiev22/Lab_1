money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

capital = money_capital + salary

month = 0 # количество месяцев, которое можно прожить

# TODO Оформить решение

for i in range(capital):
    month = capital - spend
    spend = spend * 1.05

print(month)

