from datetime import datetime

def save_log():
    type = "ValueError"
    match type:
        case "ValueError":
            with open("./error.log", "a") as file:
                file.write(f"ValueError: Order's value must be a float number ({datetime.now()})\n")
                print("Insert a valid number\n")
        case "InvalidNameLength":
            with open("../error.log", "a") as file:
                file.write(f"InvalidNameLength: Customer's or seller's name must be at least 3 characters length ({datetime.now()})\n")
                print("Insert a valid name\n")