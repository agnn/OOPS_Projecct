# This module will take type of any category
from logging_class import lg

def type():
    'Call function to enter description'
    lg.info("function called")

    try:
        s = input("Please enter type")
        lg.info("Type : %s", s)
        return s

    except Exception as e:
        lg.error(e)