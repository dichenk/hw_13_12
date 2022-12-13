class Item:
    def __init__(self, name, price, quantity=0):
        self.__check(name, price, quantity)
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})'
 
    @staticmethod
    def __check(name, price, quantity):
        if not isinstance(name, str):
            raise TypeError('Название товара должно быть строкой.')
        if not (isinstance(price, int) and price > 0):
            raise TypeError('Цена товара должна быть положительным числом.')
        if not (isinstance(quantity, int) and quantity >= 0):
            raise TypeError('Количество товара должно быть натуральным числом.')

class Phone(Item):
    def __init__(self, name, price, quantity, broken_phones):
       super().__init__(name, price, quantity)
       self.broken_phones = broken_phones

    def __str__(self):
        return f'{self.__class__.__name__}({self.name}, {self.price}, {self.quantity}, {self.broken_phones})'



print(Phone('phone', 18000, 5, 16))
print(Phone('phone', 1, 0, 10))
