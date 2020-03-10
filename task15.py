def year():
    age = int(input('Введите ваш день рождение: '))
    for i in range (age % 2 , age + 2, 2):
        return(i)
print(year())