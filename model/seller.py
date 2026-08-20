class Seller:
    def __init__(self, identifier, name, email):
        self.identifier = identifier
        self.name = name
        self.email = email
        self._orders = []

    @property
    def identifier(self):
        return self._identifier

    @identifier.setter
    def identifier(self, identifier: int):
        if not identifier:
            raise ValueError("Id is missing")
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
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str):
        if not email:
            raise ValueError("Email is missing")
        # Implement regex
        self._email = email

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value: float):
        if value < 1:
            raise ValueError("Value must be more than 0")
        self._total += value