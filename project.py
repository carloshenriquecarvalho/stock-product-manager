from datetime import datetime

def main():
    print("Previous orders:")
    get_all_orders()
    while True:
        print("Create a new order or press .exit to quit")
        customer_name = get_name("customer")
        if customer_name == ".exit":
            print("Good Bye!")
            break
        
        seller_name = get_name("seller")
        if seller_name == ".exit":
            print("Good Bye!")
            break
        
        if customer_name == False:
             continue
        try:
            order_value = float(input("What's the order value? "))
        except ValueError:
            # save_log("ValueError")
            continue
        else:
            save_order(customer_name, seller_name, order_value)
            print("Order saved successfully!\n")

# def save_log(type):
    # match type:
    #     case "ValueError":
    #         with open("log_error.txt", "a") as file:
    #             file.write(f"ValueError: Order's value must be a float number ({datetime.now()})\n")
    #             print("Insert a valid number\n")
    #     case "InvalidNameLength":
    #                 with open("log_error.txt", "a") as file:
    #                     file.write(f"InvalidNameLength: Customer's or seller's name must be at least 3 characters length ({datetime.now()})\n")
    #                     print("Insert a valid name\n")

def save_order(customer_name, seller_name, order_value):
    with open("orders.txt", "a") as file:
        file.write(f"Name: {customer_name}, Seller: {seller_name}, Value: {order_value:.2f}\n")

def get_name(for_):
    name = input(f"What's {for_}'s name? ").strip()
    
    if len(name) < 3:
        # save_log("InvalidNameLength")
        return False
    return name

def get_all_orders():
     with open("orders.txt") as file:
          for line in file:
               print(line.rstrip())

if __name__ == "__main__":
    main()