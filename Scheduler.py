

def readfile():
    job_file = open("jobs.dat", "r")
    jobs = []
    line = job_file.readline()
    while line:
        line=line.split()
        jobs.append(Job(line[0], line[1], line[2]))
        line = job_file.readline()
    print(jobs[0].job_id)


def fifo(jobs):
    pass


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
    readfile()
