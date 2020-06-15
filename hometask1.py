# task 1
print('Task 1')
N = int(input("Введите число до 100: "))
s = []
for i in range (N):
    s.append(i)
    if i % 2 == 0:
        print(i)
print(s)

#task 2
print('Task 2')
countries = {
    'USA': 'Washington',
    'USSR': 'Moscow',
    'Ukraine': 'Kyiv'
}
list_countries = list(['France', 'USA', 'Germany'])

for i in range(len(list_countries)):
    if countries.get(list_countries[i]) != None:
        print(countries.get(list_countries[i]))

#task3
print('Task 3')
N = 100
s = []
for i in range(1, N):
    if i % 3 == 0 and i % 15 != 0:
        print('Fizz')
    elif i% 5 == 0 and i % 15 != 0:
        print('Buzz')
    elif i % 15 == 0:
        print('FizzBuzz')
    else:
        print(i)

#task4
print('Task 4')
amount = int(input('Введите сумму депозита: '))
years = int(input('Введите кол-во лет: '))
interest = int(input('Введите ставку %%: '))
print('Сумма к выплате: ', amount*interest*years/100+amount)