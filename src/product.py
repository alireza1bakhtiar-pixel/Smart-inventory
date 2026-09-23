class Product:
    def __init__(self, id, name, category, price, quantity):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("ID must be positive and integer")
        self.__id = id

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("price cant be negetive number !!")
        
        self.__price = price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cant be less than zero !!")
        
        self.__quantity = quantity

    def __str__(self):
        return (f"name: {self.name} \n"
        f"ID: {self.id}\n"
        f"category: {self.category} \n"
        f"price: {self.price} \n"
        f"quantity: {self.quantity}")
    
