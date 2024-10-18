print('Otpravka priglasheniy...\n')

gosti=['Pepa','Pepega','Pepegus']
for n in gosti:
    print(f'{n.title()} vi priglasheni')

print(f'\n{gosti[0]} ne priedet')

gosti.remove('Pepa')
print('Poisk novogo gostya...\n')

gosti.insert(0, 'Pipa')
for n in gosti:
    print(f'{n.title()} vi priglasheni')

print('\nRasshirenie spiska\nPoisk novogo gostya...\n')

gosti.insert(0, 'Grogu')
gosti.insert(2, 'Groot')
gosti.append('Veyder')
for n in gosti:
    print(f'{n.title()} vi priglasheni')

print('\nogranichenie: max 2 gostya\n')

print(f'{gosti[5]} vi udaleni')
gosti.pop(5)
print(f'{gosti[4]} vi udaleni')
gosti.pop(4)
print(f'{gosti[3]} vi udaleni')
gosti.pop(3)
print(f'{gosti[2]} vi udaleni\n')
gosti.pop(2)

for g in gosti:
    print(f'{g} priglashenie v sile')

print('\notmena priglasheniy...\n')
del gosti[:]

print(f'spisok gostei{gosti}\n... spisok pust')

    


    



