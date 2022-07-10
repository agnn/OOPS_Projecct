from logging_class import lg
from Students import student

lg.info("Student survey: ")
print("Please enter the below details in specified format")
userid = input("please enter user id")
password = input("please enter password")
objstudent = student.studentdetails(userid,password)
objstudent.basicdetails()
