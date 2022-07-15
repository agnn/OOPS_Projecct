#import custom packages and modules
from logging_class import lg
from Courses import description
from Courses import duration
from Courses import title
from Courses import price
# this module will enter details of any course into log, demonstrate use of simple objects,classes,methods.

def course_record():

    try:
        lg.info("Course details: ")
        print("Please enter the below details in specified format")

        #objects of classes
        objCourses = title.title()
        objdes = description.description()
        objprice = price.price()
        objdur = duration.duration()

        #function call through object
        objCourses.title()
        objdes.description()
        objprice.price()
        objdur.duration()

    except Exception as e:

        lg.error(e)