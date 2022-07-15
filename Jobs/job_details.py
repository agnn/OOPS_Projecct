from logging_class import lg

class job:
    'class with methods related to job detail record input , constructor defined takes jobid as parameter'
    def __init__(self,jobid):
        'constructor to take job id ,default parameter set to zero'
        lg.info("Constructor initialized")

        self.jobid = jobid

    def job_title(self):
        'Function to return job title'

        try:
            title = input("Job title : ")
            lg.info("Job title %s", title)

        except Exception as e:

            lg.error(e)
        return title

    def job_details(self):
        'Function to enter details of job, '

        try:

            title = job.job_title(self) #variable created to store return value of  method job_title in job_details
            des = input('enter description :')
            exp = input('experience required :')
            location = input('location : ')

            lg.info("Job Title : %s, Description : %s , Experience : %s , Location : %s",title,des,exp,location)

        except Exception as e:

            lg.error(e)


