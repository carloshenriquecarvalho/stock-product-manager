from config.register import Register
from model.order import Order
from model.product import Product
from model.customer import Customer
from model.seller import Seller

import json

def test_save_product(tmp_path):
    product = Product(1, "Mouse", 65.45)
    file_path = Register.save(
        data=product,
        entity="products",
        directory=tmp_path
    )

    assert file_path.exists()

    with file_path.open("r", encoding="utf8") as file:
        saved_product = json.load(file)

    assert saved_product == product.to_dict()

def test_save_seller(tmp_path):
    seller = Seller(1, "Xavier", "marquin@gmail.com")
    file_path = Register.save(
        data=seller,
        entity="seller",
        directory=tmp_path
    )

    assert file_path.exists()

    with file_path.open("r", encoding="utf8") as file:
        saved_seller = json.load(file)

    assert saved_seller == seller.to_dict()

def test_save_customer(tmp_path):
    customer = Customer(1, "Carlos")
    file_path = Register.save(
        data=customer,
        entity="customer",
        directory=tmp_path
    )

    assert file_path.exists()

    with file_path.open("r", encoding="utf8") as file:
        saved_customer = json.load(file)

    assert saved_customer == customer.to_dict()

def test_save_order(tmp_path):
    order = Order(1, 1, 1)

    file_path = Register.save(
        data=order,
        entity="orders",
        directory=tmp_path
    )

    assert file_path.exists()

    with file_path.open("r", encoding="utf8") as file:
        saved_order = json.load(file)

    assert saved_order == order.to_dict()
