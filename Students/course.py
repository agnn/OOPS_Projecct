from logging_class import lg

class courseenroll():
    'this class will take details regarding courses enrolled, RETURNS number of courses enrolled'

    def course_enrolled(self):
        lg.info("Function called")

        try:

            _course = int(input("Number of courses enrolled : ")) # private variable defined
            lg.info("Courses enrolled :  %s" , _course)

        except Exception as e:

            lg.error(e)

        return _course