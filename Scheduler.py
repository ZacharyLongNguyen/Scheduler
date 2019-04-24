import numpy as np

def readfile():
    job_file = open("jobs.dat", "r")
    job = []
    x = 0
    line = job_file.readline()
    while line:
        line=line.split()
        job.append(Job(line[0],line[1],line[2]))
        line = job_file.readline()
    print(job[0].job_id)

    

class Job:
    def __init__(self, job_id, arrival_time, duration):
        self.job_id = job_id
        self.arrival_time = arrival_time
        self.duration = duration





if __name__ == "__main__":
    readfile()