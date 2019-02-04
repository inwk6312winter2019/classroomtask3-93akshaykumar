import random as r
class Card:
    def __init__(self):
        self.__suit=[]
        self.__color=('Heart','Diamond','clove','Spade')
        self.__number=(14,2,3,4,5,6,7,8,9,10,11,12,13)
        for color in self.__color:
            for num in self.__number:
                self.__suit.append(color+'-'+str(num))
        r.shuffle(self.__suit)

    def getsuit(self):
        return self.__suit

class Player(Card):
    def __init__(self,pcards=[]):
        pass





c1=Card()


print('The suffled deck::',c1.getsuit())
