from logging_class import lg

class internship():
    'this class will take details regarding internship'

    def intership_taken(self):
        'RETURNS number of internship'
        try:

            _intern = int(input("Number of  Internship enrolled: "))
            lg.info("Internship enrolled :  %s", _intern)


        except Exception as e:

            lg.error(e)

        return  _intern