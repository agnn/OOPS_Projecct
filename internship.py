from logging_class import lg
from Courses import description
from Courses import title
from Internship import type
from Internship import diffcultylevel

#this module take details regarding intership and writes to log file, demonstrate workign of package ,module,class ,objects ,fucntions

def internship():

    try:

        lg.info("Internship details: ")
        print("Please enter the below details in specified format")

        objCourses = title.title()
        objdes = description.description()


        objCourses.title()
        objdes.description()
        type.type()
        diffcultylevel.difficultylevel()

    except Exception as e:

        lg.error(e)