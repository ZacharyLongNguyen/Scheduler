def readfile():
    job_file = open("jobs.dat", "r")
    jobs = []
    line = job_file.readline()
    while line:
        line = line.split()
        jobs.append(Job(int(line[0]), int(line[1]), int(line[2])))
        line = job_file.readline()
    return jobs

def getStart(job):
    start = 0
    total = 0
    job[0].start = job[0].arrival_time
    for i in range (1, len(job)):
        total = total + job[i - 1].duration
        if(job[i].arrival_time > total):
            job[i].start = job[i].arrival_time
            continue
        job[i].start = job[i - 1].duration + start
        start = start + job[i - 1].duration

def getEnd(job):
    job[0].completion = job[0].duration + job[0].arrival_time
    for i in range (1, len(job)):
        job[i].completion = job[i].start + job[i].duration

def getResponse(job):
    response = 0
    total = 0
    job[0].response_time = job[0].arrival_time
    for i in range (1, len(job)):
        total = total + job[i - 1].duration
        if(job[i].arrival_time > total):
            job[i].response_time = job[i].arrival_time
            continue
        job[i].response_time = job[i - 1].duration + response
        response = response + job[i - 1].duration

def printTable():
    print("ID \t ARRIVAL \t DURATION \t START \t END \t TOTAL \t RESPONSE")
    for i in range (0, len(jobs)):
        print(jobs[i].job_id, end="\t")
        print(jobs[i].arrival_time, end="\t\t")
        print(jobs[i].duration, end="\t\t")
        print(jobs[i].start, end="\t")
        print(jobs[i].completion, end="\t")
        print(jobs[i].response_time)


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
    getStart(job)
    getEnd(job)
    getResponse(job)
    print("FIFO Table: ")
    printTable()

        # TODO calc turn around time


def sjf(jobs):
    job = jobs
    for i in range(0, len(job)):
        for j in range (i, len(job)):
            if(job[i].arrival_time == job[j].arrival_time and job[j].duration < job[i].duration):
                temp = job[j]
                job[j] = job[i]
                job[i] = temp
    getStart(job)
    getEnd(job)
    getResponse(job)
    print("SJF Table:")
    printTable()


def bjf(jobs):
    job = jobs
    for i in range(0, len(job)):
        for j in range(i, len(job)):
            if(job[i].arrival_time == job[j].arrival_time and job[j].duration > job[i].duration):
                temp = job[j]
                job[j] = job[i]
                job[i] = temp
    getStart(job)
    getEnd(job)
    getResponse(job)
    print("BJF Table:")
    printTable()


def stcf(jobs):
    rt = [0] * (len(jobs) - 1)
    for i in range(len(jobs) - 1):
        rt[i] = jobs[i].duration
    print("STCF Table:")
    printTable()

def rr(jobs):
    print("RR Table:")
    printTable()


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
    sortByArrival(jobs)
    fifo(jobs)
    print("")
    sjf(jobs)
    print("")
    bjf(jobs)
    print("")
    stcf(jobs)
    print("")
    rr(jobs)
