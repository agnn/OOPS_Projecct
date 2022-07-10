# This module will take the duration of any category
from logging_class import lg
class duration:
    def duration(self):
        'Call function to enter duration'
        lg.info("function called")

        try:

            s = input("Please enter duration")
            lg.info("Duration : %s", s)
            return s

        except Exception as e:
            lg.error(e)