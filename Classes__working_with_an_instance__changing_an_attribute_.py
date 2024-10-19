class Restoran():
    
    def __init__(self, r_name, r_kuhnya):
        self.r_name = r_name
        self.r_kuhnya = r_kuhnya
        self.num_gosti = 0
        
    def inf_restoran(self):
        print(f'Название ресторана: {self.r_name}\nКухня: {self.r_kuhnya}\n')
        
    def open_restoran(self):
        print(f'Ресторан "{self.r_name}" открыт!\n_______________________\n')
        
    def update_gosti(self, num_gosti):
        if num_gosti < 0:
            print('Вы кого-то убили?')
        else:
            self.num_gosti += num_gosti
                    
    def gosti(self):
        print(f'Гостей обсулжено: {self.num_gosti}\n...\n')     

restoran = Restoran('Эшь', 'Вкусная')
restoran_2 = Restoran('НеЭшь', 'НеОчВкусная')

restoran.inf_restoran()
restoran.open_restoran()
restoran.update_gosti(-1)
restoran.gosti()

restoran_2.inf_restoran()
restoran_2.open_restoran()
restoran_2.update_gosti(8)
restoran_2.gosti()









