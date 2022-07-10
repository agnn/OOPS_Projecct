# This module will take phone number and email id details
from logging_class import lg

def communication():
    'Call function to enter phone number and email id '
    lg.info("function called")

    try:
        _phonenumber = input("Please enter contact number")
        _emailid = input("Please enter email id")
        lg.info("contact number : %s ", _phonenumber)
        lg.info("email id :%s ", _emailid)


    except Exception as e:
        lg.error(e)