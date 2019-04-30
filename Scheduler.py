

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
    print("ID \t ARRIVAL \t DURATION")
    for i in range (0, len(jobs)):
        print(jobs[i].job_id, end="\t")
        print(jobs[i].arrival_time, end="\t\t") 
        print(jobs[i].duration)


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
    printTable()

        # TODO calc turn around and response time
        #

    test = 1



def sjf(jobs):
    time = 0
    job = jobs
    time = 0
    for i in range(0, len(job)):
        for j in range (i, len(job)):
            if(job[j].duration < job[i].duration):
                temp = job[j]
                job[j] = job[i]
                job[i] = temp
    print("SJF Table:")
    printTable()


def bjf(jobs):
    time = 0
    job = jobs
    time = 0
    for i in range(0, len(job)):
        for j in range(i, len(job)):
            if(job[j].duration > job[i].duration):
                temp = job[j]
                job[j] = job[i]
                job[i] = temp
    print("BJF Table:")
    printTable()


def stcf(jobs):
    print("STCF Table:")
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
    fifo(jobs)
    sjf(jobs)
    bjf(jobs)
    stcf(jobs)
