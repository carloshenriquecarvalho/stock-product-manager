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
        directory.mkdir(parents=True, exist_ok=True)

        file_path = directory / f"{entity}.json"

        try:
            records = cls._read_json(file_path)

            if not isinstance(records, list):
                raise TypeError("The JSON root must be a list")

            records.append(data.to_dict())

            with file_path.open("w", encoding="utf-8") as file:
                json.dump(
                    records,
                    file,
                    indent=4,
                    ensure_ascii=False
                )

            print("File saved!")
            return file_path

        except (TypeError, ValueError) as error:
            print(f"Serialization error: {error}")
            return None

    @staticmethod
    def _read_json(file_path):

        if not file_path.exists():
            return []
        try:
            with file_path.open("r", encoding="utf-8") as file:
                records = json.load(file)

            if isinstance(records, list):
                return records

            if isinstance(records, dict):
                return [records]

            raise ValueError(
                "JSON content must be a list or dictionary"
            )

        except json.JSONDecodeError:
            return []

    def find(entity, directory="./data"):
        directory = Path(directory)
        file_path = directory / f"{entity}.json" 

        with file_path.open("r", encoding="utf8") as file:
            data = json.load(file)

        if entity == "products":
            return [
                Product(
                    item["identifier"],
                    item["name"],
                    item["value"]
                )
                for item in data
            ]

        if entity == "orders":
            return [
                Order(
                    item["identifier"],
                    item["seller_identifier"],
                    item["customer_identifier"]
                )
                for item in data
            ]

        if entity == "customers":
            return [
                Customer(
                    item["identifier"],
                    item["name"]
                )
                for item in data
            ]

        if entity == "sellers":
            return [
                Seller(
                    item["identifier"],
                    item["name"]
                )
                for item in data
            ]