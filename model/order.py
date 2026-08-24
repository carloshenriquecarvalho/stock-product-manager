from model.product import Product

class Order:
    def __init__(self, identifier, seller_identifier, customer_identifier):
        self.identifier = identifier
        self.seller_identifier = seller_identifier
        self.customer_identifier = customer_identifier
        self._products = []

    @property
    def identifier(self):
        return self._identifier

    @identifier.setter
    def identifier(self, identifier: int):
        if not identifier:
            raise ValueError("identifier is missing")
        self._identifier = identifier

    @property
    def customer_identifier(self):
        return self._customer_identifier

    @customer_identifier.setter
    def customer_identifier(self, identifier: int):
        if not identifier:
            raise ValueError("identifier is missing")
        self._customer_identifier = identifier

    def add_product(self, product):
        if not isinstance(product, Product):
            raise NameError("Product must be a Product Object")
        self._products.append(product)


    # Get total value
    def get_total(self):
        total = 0
        # Get all Products' value
        for product in self._products:
            total += product.value
        return total

    def __str__(self):
        for product in self._products:
            return f"{product}"

    def to_dict(self):
        return {
            "identifier": self._identifier,
            "seller_identifier": self.seller_identifier,
            "customer_identifier": self.customer_identifier,
            "products": [product.to_dict() for product in self._products]
        }