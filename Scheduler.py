

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


def sortByArrival(job):
    for i in range(0, len(job) - 1):
        for j in range(0, len(job) - i - 1):
            if (job[j].arrival_time > job[j + 1].arrival_time):
                temp = job[j]
                job[j] = job[j + 1]
                job[j + 1] = temp
    return job


def fifo(jobs):
    i = 0
    time = 0
    job = jobs
    job = sortByArrival(job)
    while i < len(job):
        job[i].start = time
        job[i].completion = time + job[i].duration
        time = time + job[i].duration
        i += 1
        print("FIFO table: ")

        # TODO calc turn around and response time
        #

    test = 1



def sjf(jobs):
    #time = 0
    #job = jobs
    #job = sortByArrival(job)
    #time = 0
    #if(job[0].arrival_time > time):
    #    time = job[0].arrival_time
    #job[0].start = time
    #for i in range(1, len(job) - 1):
    #    for j in range((i + 1), )


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
