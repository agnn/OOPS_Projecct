# This module will take description of any category
from logging_class import lg
class description:
    def description(self):
        'Call function to enter description'
        lg.info("function called")

        try:
            s = input("Please enter description")
            lg.info("Description : %s", s)
            return s

        except Exception as e:
            lg.error(e)