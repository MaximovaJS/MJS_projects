# Задача 5
# Зарплата сотрудника составляет salary руб., 
# Расходы на проживание превышают зараплату и составляют expenses руб. в месяц. 
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Напишите скрипт расчета суммы денег, которую необходимо взять в долг, 
# чтобы можно было прожить ближайший год (12 месяцев).
# Формат вывода:
# Необходимо взять в долг ХХХ.ХХ рублей

salary, expenses = 10000, 12000

month= [1,2,3,4,5,6,7,8,9,10,11,12]
month_exp=[]
month_exp.append(expenses)
all_exp=0

for i in month:
    month_exp.append(month_exp[i-1]*1.03)
    all_exp=all_exp+month_exp[i]


credit=round(abs(salary*12-all_exp),2)

print('Необходимо взять в долг', credit, 'рублей')

# Хорошо. Можно еще через while
# Решение 2
salary, expenses = 10000, 12000

i = expenses - salary
m = 0
debt = 0
while m < 12:
    mx = i * (1.03 ** m)
    debt += mx
    m += 1
print(f'Необходимо взять в долг {round(debt, 2)} рублей')
