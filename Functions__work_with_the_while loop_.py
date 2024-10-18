def make_album_2(name_aut, name_alb):
    muz = {'aut': name_aut, 'alb': name_alb }
    return muz

while True:
    
    print('\nУкажите информацию об альбоме:')
    print('Для выхода из программы напишите "q"\n')
    
    name_aut = input('Укажите имя автора: \n')
    if name_aut == 'q':
        break
    name_alb = input('Укажите название альбома: \n')
    if name_alb == 'q':
        break
    
    
    album = make_album_2(name_aut , name_alb)

    print(album)




