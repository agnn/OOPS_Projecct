# This file when executed will run a series of operation.
# The operations includes taking inputs from user to update/log into database/log file.
import student_record,student_record_edit,course_record,internship,password_change
from Jobs import job_details
from logging_class import lg
import sys

def exe_run():


    while True:

        try:

            print('''Please select your operation
                    1 - Add a student record
                    2 - Edit a student record
                    3 - Add a course record
                    4 - Add internship record
                    5 - Update your password
                    6 - Add job details record
                    7 - Exit''')


            response = int(input("specify : "))
            lg.info("user selected %s",response)

            if response == 1:
                exe_clr()
                student_record.student_record()
            elif response ==2:
                exe_clr()
                student_record_edit.student_recordedit()
            elif response == 3:
                exe_clr()
                course_record.course_record()
            elif response == 4:
                exe_clr()
                internship.internship()
            elif response == 5:
                exe_clr()
                password_change.password_change()
            elif response == 6:
                exe_clr()
                job_details.job.job_details(0)
            elif response == 7:
                sys.exit("Thank you")
            else:
                print("try entering only numbers related to the topics")
                continue
            exe_clr()
            print("another record ? ")
        except Exception as e:

            lg.error(e)


def exe_clr():
    print("\n"*100)


exe_run()
