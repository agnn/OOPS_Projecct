from logging_class import lg
from Courses import description
from Courses import duration
from Courses import title
from Courses import price

lg.info("Course details: ")
print("Please enter the below details in specified format")

objCourses = title.title()
objdes = description.description()
objprice = price.price()
objdur = duration.duration()

objCourses.title()
objdes.description()
objprice.price()
objdur.duration()