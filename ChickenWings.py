class Wings:
    def __init__(self, spicy = '', pieces = 0, price = 0.0):
        self.__spicy = spicy
        self.__pieces = pieces
        self.__price = price

    @property
    def spicy(self):
        return self.__spicy
    @spicy.setter
    def spicy(self, s):
        self.__spicy = s

    @property
    def pieces(self):
        return self.__pieces
    @pieces.setter
    def pieces(self, p):
        self.__pieces = p

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, p):
        self.__price = p

    def __str__(self):
        displayString = str('Sauce: {}\nPieces: {}\nPrice: ${:,.2f}'.format(
            self.__spicy,
            self.__pieces,
            self.__price))
        return displayString

if __name__ == '__main__':
    temp = Wings('Ghost Pepper', 12, 12.50)
    print(temp)

        
