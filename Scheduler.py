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
        if(job[i - 1].total - job[i].arrival_time < 0):
            job[i].response_time = 0
        else:
            job[i].response_time = job[i - 1].total - job[i].arrival_time


def getTotal(job):
    total = job[0].duration
    job[0].total = job[0].duration
    for i in range (1, len(job)):
        total = total + job[i].duration
        job[i].total = total

def printTable():
    print("ID \t ARRIVAL \t DURATION \t START \t END \t TOTAL \t RESPONSE")
    for i in range (0, len(jobs)):
        print(jobs[i].job_id, end="\t")
        print(jobs[i].arrival_time, end="\t\t")
        print(jobs[i].duration, end="\t\t")
        print(jobs[i].start, end="\t")
        print(jobs[i].completion, end="\t")
        print(jobs[i].total, end="\t")
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
    getTotal(job)
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
    getTotal(job)
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
    getTotal(job)
    getResponse(job)
    print("BJF Table:")
    printTable()

'''
def stcf(jobs):
    job = jobs
    wait = [0] * (len(jobs) - 1)
    rt = [0] * (len(jobs) - 1)
    for i in range(len(jobs) - 1):
        rt[i] = jobs[i].duration
        wait[i] = 0
    complete = 0
    minm = 999999999
    time = 0
    short = 0
    while (complete != len(jobs) - 1):
        for j in range(len(jobs) - 1):
            if ((jobs[j].arrival_time <= time) and (rt[j] < minm) and rt[j] > 0):
                minm = rt[j]
                short = j
                check = True
            if (check == False):
                time += 1
                continue
            rt[short] -= 1
            minm = rt[short]
            if (minm == 0):
                minm = 99999999
            if (rt[short] == 0):
                complete += 1
                check = False
                fint = time + 1
                if (wait[short] < 0):
                    wait[short] = 0
            time += 1
    for k in range(len(jobs) - 1):
        job.turn_around = jobs[k].duration + wait[k]
    print("STCF Table:")
    printTable()

def rr(jobs):
    print("RR Table:")
    printTable()
'''

class Job:
    def __init__(self, job_id, arrival_time, duration):
        self.job_id = job_id
        self.arrival_time = arrival_time
        self.duration = duration

        self.start = None
        self.completion = None
        self.response_time = None
        self.turn_around = None
        self.total = None

    def __repr__(self):
        return "job_id: {}, arrival_time: {},duration: {},response_time{},completion{},start{},turn_around{}"\
            .format(self.job_id, self.arrival_time, self.duration, self.response_time, self.completion, self.start, self.turn_around)


if __name__ == "__main__":
    jobs = readfile()
    sortByArrival(jobs)
    fifo(jobs)
    print("")
    sjf(jobs)
    print("")
    bjf(jobs)
    print("")
   # stcf(jobs)
    #print("")
   # rr(jobs)
