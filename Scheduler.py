

def readfile():
    job_file = open("jobs.dat", "r")
    jobs = []
    line = job_file.readline()
    while line:
        line = line.split()
        jobs.append(Job(int(line[0]), int(line[1]), int(line[2])))
        line = job_file.readline()
    return jobs
    #TODO: Create a function to print the table

def printTable():
    #for i in range (0, len(jobs)):
    pass


def fifo(jobs):

    i = 0
    time = 0
    while i < len(jobs):
        job = jobs[i]
        job.start = time
        job.completion = time + job.duration
        time = time + job.duration
        i += 1
        print("FIFO table: ")

        # TODO calc turn around and response time
        #

    test = 1



def sjf(jobs):
    pass


def bjf(jobs):
    pass


def stcf(jobs):
    pass


class Job:
    def __init__(self, job_id, arrival_time, duration):
        self.job_id = job_id
        self.arrival_time = arrival_time
        self.duration = duration

        self.start = None
        self.completion = None
        self.response_time = None
        self.turn_around = None


if __name__ == "__main__":
    jobs = readfile()
    fifo(jobs)
