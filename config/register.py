import json
from model.product import Product
from model.customer import Customer
from model.seller import Seller
from model.order import Order
from pathlib import Path
 
class Register:
    
    @classmethod
    def save(cls, data, entity, directory="./data"):
        directory = Path(directory)
        file_path = directory / f"{entity}.json"
        try:
            directory.mkdir(parents=True, exist_ok=True)

            with file_path.open("w", encoding="utf8") as file:
                json.dump(data.to_dict(), file, indent=4, ensure_ascii=False)

            print("File saved! ")
        except (TypeError, ValueError) as e:
            print(f"Serialization error: {e}")
        return file_path

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