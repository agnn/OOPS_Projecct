from logging_class import lg
import Contact.communcation as com
from Students.affiliates import affiliates
from Students.course import courseenroll
from Students.internship import internship
import writedb.writedb as wb

class studentdetails(courseenroll,internship,affiliates) :
    'Example of multiple inheritence importing class from package '

    def __init__(self,userid,password):
        'Constructor to take userid and password'

        try:
            lg.info("Constructor called")
            self.userid = userid
            self.__password = password      #protected variable

            lg.info("Constructor call success")

        except Exception as e:

            lg.error(e)

    def basicdetails(self):
        'To enter basic details of students'
        lg.info("Function called")

        try:

            #use of private variables
            lg.info("User : %s",self.userid)
            __name = input("Enter name : ")
            lg.info("name : %s", __name)
            __dob = input("Enter date of birth in DD/MM/YY format")
            lg.info("Date of birth : %s", __dob)
            __gender = input("Enter gender")
            lg.info("Gender : %s", __gender)

            __mob = com.communication.communication_mobile(self)
            __email = com.communication.communication_email(self)
            __courses = courseenroll.course_enrolled(self)
            __internship = internship.intership_taken(self)
            __aff = affiliates.aff(self)

            #writing to database
            wb.insert_values(self.userid,__name,__dob,__gender,__mob,__email,__courses,__internship)
        except Exception as e:

            lg.error(e)

    def password_change(self,newpassword):
        'This will update the _password'
        # encapsulation explained to modify private variable __password
        try:
            self.__password = newpassword
            lg.info("new password updated is %s", self.__password)
        except Exception as e:
            lg.error(e)

class student_edit(studentdetails):
    'this class will override fucntions of studentdetails class methods'


    def basicdetails(self):
        'to edit any record'
        #to demonstrate method overriding

        try:
            lg.info("User : %s", self.userid)
            print("Please mention what you want to edit\n1 - Name\n2 - date of birth\n3 - Gender")
            editdetail = int(input())
            newvalue = input("Enter new value : ")
            if editdetail == 1:
                lg.info("Name updated : %s",newvalue)
            elif editdetail == 2:
                lg.info("D.O.B updated : %s", newvalue)
            elif editdetail == 3:
                lg.info("Gender : %s", newvalue)
            else:
                self.basicdetails()
        except Exception as e:
            lg.error(e)

