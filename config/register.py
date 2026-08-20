import json
from datetime import datetime
from decimal import Decimal

class Register:
    def custom_serializer(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        raise TypeError(f"Type {type(obj)} not serializable")
    
    @classmethod
    def save(cls, data, entity):
        try:
            with open(f"./data/{entity}.json", "w", encoding="utf8") as file:
                json.dump(data, file, default=cls.custom_serializer, indent=4, ensure_ascii=False)

            print("File saved! ")
        except (TypeError, ValueError) as e:
            print(f"Serialization error: {e}")