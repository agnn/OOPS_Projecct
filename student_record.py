from logging_class import lg
from Students import student

def student_record():
    'To enter and write details to database, student basis details are recorded'

    try:
        lg.info("Student survey: ")
        print("Please enter the below details in specified format")
        userid = input("please enter user id")
        password = input("please enter password")
        objstudent = student.studentdetails(userid,password)
        objstudent.basicdetails()

    except Exception as e:
        lg.error(e)
