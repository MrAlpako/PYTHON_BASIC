﻿inf_hum_1={
    'Имя:': 'Пепа',
    'Фамилия:': 'Пепега',
    'Возраст:': '26',
    'Город:': 'Москва'
    }

inf_hum_2={
    'Имя:': 'JJ',
    'Фамилия:': 'JJJ',
    'Возраст:': '21',
    'Город:': ['Питер', 'Краснодар']
    }

inf_hum_3={
    'Имя:': 'QQ',
    'Фамилия:': 'QQQ',
    'Возраст:': '62',
    'Город:': 'Саратов'
    }

humans=[inf_hum_1, inf_hum_2, inf_hum_3]
for i in humans:
    for k,v in i.items():
        print(k,v)
        
        