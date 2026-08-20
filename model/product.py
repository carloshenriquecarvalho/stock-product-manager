class Product:
    def __init__(self, identifier, name, value):
        self.identifier = identifier
        self.name = name
        self.value = value

    @property
    def identifier(self):
        return self._identifier

    @identifier.setter
    def identifier(self, identifier: int):
        if not identifier:
            raise ValueError("identifier is missing")
        self._identifier = identifier

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if not name:
            raise ValueError("Name is missing")
        self._name = name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: float):
        if value < 1:
            raise ValueError("Value must be more than 0")
        self._value = value

    def __str__(self):
        return f"Name: {self.name} \nValue: {self.value}"