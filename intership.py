from logging_class import lg
from Courses import description
from Courses import title
from Internship import type
from Internship import diffcultylevel


lg.info("Internship details: ")
print("Please enter the below details in specified format")

objCourses = title.title()
objdes = description.description()


objCourses.title()
objdes.description()
type.type()
diffcultylevel.difficultylevel()

lg.info("Comment to check push to github")