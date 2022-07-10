from logging_class import lg

class job:

    def __init__(self,jobid):
        lg.info("Constructor initialized")

        self.jobid = jobid

    def job_title(self):
        'Function to return job title'

        try:
            title = input("Job title : ")
            lg.info("Job title %s", title)

        except Exception as e:

            lg.error(e)

    def job_details(self):
        'Function to enter details of job'

        try:

            des = input('enter description :')
            exp = input('experience required :')
            location = input('location : ')

            lg.info("Description : %s , Experience : %s , Location : %s",des,exp,location)

        except Exception as e:

            lg.error(e)