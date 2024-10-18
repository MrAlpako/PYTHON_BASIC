def hozyain_lesa(*les):
    for l in les:
        print(l)
    
hozyain_lesa('У меня есть нож, есть арбалет', 'Они служат мне уже тысячу лет', 
          'У меня есть лес, и это мой дом','Всю свою жизнь обитаю я в нём.')

print('\n')

def spisok(**user):
    return user

spisok = spisok(Имя = 'Pepa', Фамилия = 'Pepega', Возраст = '26', Рост = '185')

print(spisok)