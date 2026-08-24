import json
from model.product import Product
from model.customer import Customer
from model.seller import Seller
from model.order import Order
 
class Register:
    
    @classmethod
    def save(cls, data, entity):
        try:
            with open(f"./data/{entity}.json", "w", encoding="utf8") as file:
                json.dump(data.to_dict(), file, indent=4, ensure_ascii=False)

            print("File saved! ")
        except (TypeError, ValueError) as e:
            print(f"Serialization error: {e}")

    def deserialize_data(entity):
        data = json.load(f"{entity}".json)

        if entity == "product":
            return [
                Product(
                    item["identifier"],
                    item["name"],
                    item["value"]
                )
                for item in data
            ]

        if entity == "order":
            return [
                Order(
                    item["identifier"],
                    item["seller_identifier"],
                    item["customer_identifier"]
                )
                for item in data
            ]

        if entity == "customer":
            return [
                Customer(
                    item["identifier"],
                    item["name"]
                )
                for item in data
            ]

        if entity == "seller":
            return [
                Seller(
                    item["identifier"],
                    item["name"]
                )
                for item in data
            ]