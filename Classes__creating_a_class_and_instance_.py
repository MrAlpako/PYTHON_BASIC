class Restoran():
    
    def __init__(self, r_name, r_kuhnya):
        self.r_name = r_name
        self.r_kuhnya = r_kuhnya
        
    def des_restoran(self):
        print(f'Название ресторана: {self.r_name}\nКухня: {self.r_kuhnya}\n')
        
    def open_restoran(self):
        print(f'Ресторан "{self.r_name}" открыт!\n')
        
restoran = Restoran('Эшь', 'Вкусная')
restoran_2 = Restoran('НеЭшь', 'НеОчВкусная')

restoran.des_restoran()
restoran.open_restoran()

restoran_2.des_restoran()
restoran_2.open_restoran()