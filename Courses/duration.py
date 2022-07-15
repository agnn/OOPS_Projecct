# This module will take the duration of any category
from logging_class import lg
class duration:
    'Class containing methods related to course duration, No constructor defined'

    def duration(self):
        'Call function to enter duration, RETURNS duration'
        lg.info("function called")

        try:

            s = input("Please enter duration") #local variable
            lg.info("Duration : %s", s)
            return s

        except Exception as e:
            lg.error(e)