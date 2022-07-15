from logging_class import lg
from Students import student

def student_recordedit():
    'to edit a student record, explains abstraction, method override'

    try:

        lg.info("Student data edit")
        print("Please enter the below details in specified format")
        userid = input("please enter user id")
        password = input("please enter password")
        objstudentedit = student.student_edit(userid, password)
        objstudentedit.basicdetails()

    except Exception as e:

        lg.error(e)