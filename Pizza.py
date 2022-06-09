class Pizza:
    ''' Class to hold details of pizza objects '''
    
    def __init__(self, size = '' , meats = [], toppings = []):
        self.__size = size
        self.__meats = meats
        self.__toppings = toppings
        
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, s):
        self.__size = s

    @property
    def meats(self):
        return self.__meats
    @meats.setter
    def meats(self, p):
        self.__meats = p

    @property
    def toppings(self):
        return self.__toppings
    @toppings.setter
    def toppings(self, p):
        self.__toppings = p
        
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, p):
        self.__price = p

    def calc_price(self):
        price = 0
        if self.__size == 'Small':
            price = price + 8
        elif self.__size == 'Medium':
            price = price + 10
        elif self.__size == 'Large':
            price = price + 12
        temp = (len(self.__meats) + len(self.__toppings)) / 2
        price += temp
        price = price + (price * .05)

        return price
            
    def __str__(self):
        meat = ' '
        for i in self.__meats:
            meat+=str(i)+' | '
        topping  = ' '
        for i in self.__toppings:
            topping += str(i) + ' | '
        displayString = str('Size: {}\nMeats: {}\nToppings: {}\nPrice: ${:,.2f}'.format(
            self.__size,
            meat,
            topping,
            self.calc_price()))
        return displayString


        
