# This module will take price of any category
from logging_class import lg
class price:
    def price(self):
        'Call function to enter price'
        lg.info("function called")

        try:

            s = input("Please enter the price")
            lg.info("Price : %s", s)
            return s

        except Exception as e:
            lg.error(e)