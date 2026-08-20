from config.register import Register

from model.order import Order
from model.customer import Customer
from model.product import Product
from model.seller import Seller

def main():
    customer = Customer(1, "Carlos")
    seller = Seller(1, "Joaquim", "cars@gmail.com")
    product = Product(1, "Mouse", 54.32)
    product2 = Product(2, "Teclado", 101.29)

    order = Order(1, seller.identifier, customer.identifier)
    order.add_product(product)
    order.add_product(product2)

    Register.save(product2, "product")

    print(order.get_total())

    print(order)

if __name__ == "__main__":
    main()