print('Цены на билеты\n')

age=int(input('Укажиие возраст: '))

while True:
    if age < 3:
        print('Билет бесплатный')
        break
    elif age >= 3 and age <= 12:
        print('Билет стоит 100 рублей')
        break
    else:
        print('Билет стоит 200 рублей')
        break
        
    
