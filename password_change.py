from logging_class import lg
from Students import student

def password_change():

    try:
        lg.info("Password reset")
        print("Please enter the below details in specified format")

        prompt = input("do you wish to update password? Y/N : ")
        if prompt == 'Y' or prompt == 'y':
            userid = input("please enter user id")
            password = input("please enter existing password")
            objstudent = student.studentdetails(userid, password)   #object creation
            newpassword = input("Enter new password :")
            objstudent.password_change(newpassword) #encaptulation & abstraction explained together
            print("new password entered is :%s ", objstudent._studentdetails__password) #private variable called

        else:
            print("Thank you")

    except Exception as e:

        lg.error(e)
