# This module will take Title of any category
from logging_class import lg
class title:
    def title(self):
        'Call function to enter title'
        lg.info("function called")

        try:
            s = input("Please enter the title")
            lg.info("Title : %s", s)
            return s
        except Exception as e:
            lg.error(e)


