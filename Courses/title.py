# This module will take Title of any category
from logging_class import lg
class title:
    'Class containing methods related to title definition, No constructor defined'

    def title(self):
        'Call function to enter title, RETURNS title'
        lg.info("function called")

        try:
            s = input("Please enter the title") #local variable
            lg.info("Title : %s", s)
            return s
        except Exception as e:
            lg.error(e)


