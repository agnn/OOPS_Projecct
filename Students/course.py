from logging_class import lg

class courseenroll():
    'this class will take details regarding courses enrolled'

    def course_enrolled(self):
        lg.info("Function called")

        try:

            _course = list(map(int,input("Number of courses enrolled : ").split()))
            lg.info("Courses enrolled :  %s" , _course)

        except Exception as e:

            lg.error(e)
