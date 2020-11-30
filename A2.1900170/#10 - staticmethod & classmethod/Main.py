class Hero:

    __jumlah = 0;

    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1

    def getJumlah(self):
        return Hero.__jumlah

    def getJumlah1():
        return Hero.__jumlah

    
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

sniper = Hero('sniper')
print(Hero.getJumlah2())
rikimaru = Hero('rikimaru')
print(sniper.getJumlah2())
drowranger = Hero('drowranger')
print(Hero.getJumlah3())