class Drink:
     
    def __init__(self, size = '', choice = '', price = 0.0):
        self.__size = size
        self.__choice = choice
        self.__price = price
       
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, s):
        self.__size = s
        
    @property
    def choice(self):
        return self.__choice
    @choice.setter
    def choice(self, c):
        self.__choice = c

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, p):
        self.__price = p

    def __str__(self):
        displayString = str('Size: {}\nType: {}\nPrice: ${:,.2f}'.format(
            self.__size,
            self.__choice,
            self.__price))
        return displayString

if __name__ == '__main__':
    temp = Drink('Large', 'Diet Coke', 1.05)
    print(temp)

        
