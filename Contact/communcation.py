# This module will take phone number and email id details
from logging_class import lg


class communication:
    '''A BASIC CLASS WITH TWO METHODS DEFINED
        NO CONSTRUCTOR DEFINED'''

    def communication_mobile(self):
        'Call function to enter phone number , RETURNS MOBILE NUMBER'
        lg.info("function called")

        try:
            'USE OF PROTECTED VARIABLE'
            _phonenumber = input("Please enter contact number")

            lg.info("contact number : %s ", _phonenumber)


        except Exception as e:
            lg.error(e)

        return _phonenumber

    def communication_email(self):
        'Call function to enter  email id, RETURNS EMAIL ID '
        lg.info("function called")

        try:
            'USE OF PROTECTED VARIABLE'
            _emailid = input("Please enter email id")


            lg.info("email id :%s ", _emailid)


        except Exception as e:
            lg.error(e)

        return _emailid