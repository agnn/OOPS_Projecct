# This module will take description of any category
from logging_class import lg

class description:
    'Class containing methods related to course details, No constructor defined'

    def description(self):
        'Call function to enter description, RETURNS description'
        lg.info("function called")

        try:
            s = input("Please enter description") #local variable
            lg.info("Description : %s", s)
            return s

        except Exception as e:
            lg.error(e)