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
    
    def getcardfromsuit(self):
        return self.__suit.pop()

class Player:
    def __init__(self,n,suit):
        self.__pcard=[suit.getcardfromsuit() for x in range(n)]

    def mycard(self):
        return self.__pcard
        



suit=Card()

print('The Deck::',suit.getsuit())
print('======================================================================')
p1=Player(13,suit)

print('The p1 card::',p1.mycard())
p2=Player(13,suit)

print('The p2 card::',p2.mycard())
p3=Player(13,suit)

print('The p3 card::',p3.mycard())
p4=Player(13,suit)
print('The p4 card::',p4.mycard())
print('======================================================================')
print('The left deck::',suit.getsuit())
