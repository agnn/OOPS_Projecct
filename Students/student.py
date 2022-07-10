from logging_class import lg
from Contact import communcation
from Students.affiliates import affiliates
from Students.course import courseenroll
from Students.internship import internship
'''
class courseenroll():
    'this class will take details regarding courses enrolled'

    def course_enrolled(self):
        lg.info("Function called")

        try:

            _course = list(map(int,input("Number of courses enrolled : ").split()))
            lg.info("Courses enrolled :  %s" , _course)

        except Exception as e:

            lg.error(e)
class internship():
    'this class will take details regarding internship'

    def intership_taken(self):

        try:

            _intern = list(map(int,input("Number of  Internship enrolled: ").split()))
            lg.info("Internship enrolled :  %s", _intern)


        except Exception as e:

            lg.error(e)

class affiliates():


    def aff(self):
        'Affiliates class against a student'
        try:

            lg.info("This class will show affiliates details : ")

        except Exception as e:

            lg.error(e)
'''
class studentdetails(courseenroll,internship,affiliates) :
    'Example of multiple inheritence importing class from package '

    def __init__(self,userid,password):
        'Constructor to take userid and password'

        try:
            lg.info("Constructor called")
            self.__userid = userid
            self.__password = password

            lg.info("Constructor call success")

        except Exception as e:

            lg.error(e)

    def basicdetails(self):
        'To enter basic details of students'
        lg.info("Function called")

        try:
            __name = input("Enter name : ")
            lg.info("name : %s", __name)
            __dob = input("Enter date of birth in DD/MM/YY format")
            lg.info("Date of birth : %s", __dob)
            __gender = input("Enter gender")
            lg.info("Gender : %s", __gender)

            __contact = communcation.communication()
            __courses = courseenroll.course_enrolled(self)
            __internship = internship.intership_taken(self)
            __aff = affiliates.aff(self)

        except Exception as e:

            lg.error(e)



