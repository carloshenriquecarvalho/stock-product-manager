from model.order import Order

class Customer:
    def __init__(self, identifier, name):
        self.identifier = identifier
        self.name = name
        self._orders = []

    @property
    def identifier(self):
        return self._identifier

    @identifier.setter
    def identifier(self, identifier: int):
        self._identifier = identifier

    @property
    def name(self):
         return self._name

    @name.setter
    def name(self, name: str):
        if not name:
            raise ValueError("Name is missing")
        if len(name) < 3:
                    raise ValueError("Name must be at least 3 digits length")
        
        self._name = name

    @property
    def orders(self):
         return self._orders

    def add_orders(self, order):
        if not isinstance(order, Order):
              raise NotImplemented
        self._orders.append(order)


    
