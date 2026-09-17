from model.products import Product
from model.payment import (
    process_payment, CashPayment, CardPayment, WalletPayment)
from model.order import Order
from view.notification import (
    notify, EmailNotification, SMSNotification, PushNotification)
from view.screen_manager import ScreenManager


class App:
    def __init__(self):
        self.screen_manger = ScreenManager

    def main(self):
        order = Order()

        while True:
            item = input(
                "Please enter your chios : ( show , q , add , total , pay ) : ").lower()
            if item == "show":
                self.screen_manger.screen_clear()
                print(order)
                print("Number of products:", len(order))
            elif item == "add":
                self.screen_manger.screen_clear()
                name = input("Please Enter tha name of the product : ")
                price = int(input("Please Enter tha price of the product : "))
                stock = int(input("Please Enter tha stock of the product : "))
                product = Product(name=name, price=price, stock=stock)
                order.add_product(product)
            elif item == "total":
                self.screen_manger.screen_clear()
                print(f"Total of you think is : {order.total_price()}")
            elif item == "q":
                self.screen_manger.screen_clear()
                print("have good time :))")
                print(order)
                print("Number of products:", len(order))
                print(f"Total of you think is : {order.total_price()}")
                break
            elif item == "pay":
                self.screen_manger.screen_clear()
                service = input(
                    "Please enter the services of notofication : ( email , sms , push ) : ").lower()
                payment = input(
                    "Please enter the way of payment : ( cash , card , wallet ) : ").lower()
                if payment == "wallet":
                    self.screen_manger.screen_clear()
                    process_payment(WalletPayment(), order.total_price())
                elif payment == "card":
                    self.screen_manger.screen_clear()
                    process_payment(CardPayment(), order.total_price())
                else:
                    self.screen_manger.screen_clear()
                    process_payment(CashPayment(), order.total_price())
                if service == "email":
                    notify(EmailNotification(),
                           "Your payment was successful !!")
                elif service == "sms":
                    notify(SMSNotification(), "Your payment was successful !!")
                else:
                    notify(PushNotification(), "Your payment was successful !!")
            else:
                self.screen_manger.screen_clear()
                print("Please Enter your chios : ( show , q , add , total) ")
