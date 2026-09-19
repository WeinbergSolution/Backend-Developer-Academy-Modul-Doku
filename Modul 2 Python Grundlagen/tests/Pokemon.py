class Pokemon:

    def __init__(self, name,):
        self.__name = name
        self.__lebenspunkte = 42
        self.__level = 1

    def vorstellen(self):
        print(f'{self.__name}, {self.__name}!')

    def zeige_lebenspunkte(self):
        return self.__lebenspunkte

    def zeige_level(self):
        return self.__level
            

if __name__ == '__main__':
    p1 = Pokemon("Pikaschu")
    p2 = Pokemon("Schiggy")

print(p1.zeige_level())
print(p2.zeige_level())