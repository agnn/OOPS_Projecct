# This module will take price of any category
from logging_class import lg
class price:
    'Class containing methods related to course pricing, No constructor defined'

    def price(self):
        'Call function to enter price, RETURNS price'
        lg.info("function called")

        try:

            s = input("Please enter the price") #local variable
            lg.info("Price : %s", s)
            return s

        except Exception as e:
            lg.error(e)