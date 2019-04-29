

def readfile():
    job_file = open("jobs.dat", "r")
    jobs = []
    line = job_file.readline()
    while line:
        line = line.split()
        jobs.append(Job(int(line[0]), int(line[1]), int(line[2])))
        line = job_file.readline()
    for i in range(0, len(jobs) - 1): # bubble sort so that jobs is sorted earliest arrival first
        for j in range(0, len(jobs) - i - 1):
            if (jobs[j].arrival_time > jobs[j + 1].arrival_time):
                temp = jobs[j]
                jobs[j] = jobs[j + 1]
                jobs[j + 1] = temp
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
    time = 0
    job = jobs
    time = 0
    if(job[0].arrival_time )


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
