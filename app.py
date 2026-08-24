from model.product import Product
from config.register import Register

def main():
    product1 = Product(1,"Mouse", 56.98)
    product2 = Product(2,"Teclado", 149.50)

    Register.save(data=product1, entity="products")
    Register.save(data=product2, entity="products")


    response = Register.find("products")

    for i in response:
        print(i)

if __name__ == "__main__":
    main()