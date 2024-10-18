#проверка выполнения условия - попадание по цвету
alien_color_1='green'
if alien_color_1.lower() == 'green':
    print('Вы заработали 5 очков\n')
elif alien_color_1.lower() == 'yellow':
    print('Вы заработали 10 очков\n')
elif alien_color_1.lower() == 'red':
    print('Вы заработали 15 очков\n')
else:
    print('Вы промахнулись...\nПопробуйте еще раз\n')
    
#проверка выполнения условия - возраст
age=int(input('Введите возраст: '))
if age<2:
    print('младенец\n')
elif age>=2 and age<4:
    print('малыш\n')
elif age>=4 and age<13:
    print('ребенок\n')
elif age>=13 and age<20:
    print('подросток\n')
elif age>=20 and age<65:
    print('взрослый\n') 
else:
    print('пожилой человек\n')

#проверка наличия в списке          
list_fruit=['Банан','Яблоко','Груша']
low_fr=[i.lower() for i in list_fruit]
for fruit in low_fr:
    fruit=input('Укажите фрукт: ') 
    if fruit in low_fr:
        print('В списке есть такой фрукт')
        break
    else:
        print('Такого фрукта нет')
