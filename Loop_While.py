#Добавление элементов в список через цикл while
top_pizza=[]
print('Для завершения программы введите "Выход"\n')

while True:
    t = input('Добавьте топпинг: ')
    if t.title() == "Выход":
        print('\n')
        break
    else:
        top_pizza.append(t)
        print(f'Топпинг {t} добавлен\n')   

for i in top_pizza:
    print(f'Список топпингов: {i}')
        

    
