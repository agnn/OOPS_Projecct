from logging_class import lg

class internship():
    'this class will take details regarding internship'

    def intership_taken(self):

        try:

            _intern = list(map(int,input("Number of  Internship enrolled: ").split()))
            lg.info("Internship enrolled :  %s", _intern)


        except Exception as e:

            lg.error(e)