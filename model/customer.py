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
         return tuple(self._orders)

    def add_orders(self, order):
        if not isinstance(order, Order):
            raise NotImplemented("Order must be of the type Order")
        self._orders.append(order)

    def to_dict(self):
        return {
            "identifier": self.identifier,
            "name": self.name,
            "orders": [order.to_dict() for order in self.orders]
        }   