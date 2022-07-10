# This module will take difficulty level of any category
from logging_class import lg

def difficultylevel():
    'Call function to select difficulty level'
    lg.info("function called")

    try:
            lg.info("Please select difficulty level as 1 = Easy, 2 = Moderate ,3 = High ")
            count = 0
            while(True and count < 3):

                s = int(input("Please select difficulty level as 1 = Easy, 2 = Moderate ,3 = High "))
                if s == 1:
                    lg.info("Difficulty  : Easy")
                    break
                elif s == 2:
                    lg.info("Difficulty  : Moderate")
                    break
                elif s == 3:
                    lg.info("Difficulty  : High")
                    break
                else:
                    lg.info("Wrong selection")
                count += 1

            if count >=3:
                lg.info("Function terminated without correct input")

            return s

    except Exception as e:
        lg.error(e)

