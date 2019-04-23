import numpy as np

def readfile():
    job_file = open("jobs.dat", "r")
    job = [[]]
    x = 0
    line = job_file.readline()
    while line:
        job_attributes = line.split()
        job_attributes = np.asarray(job_attributes)
        print(job_attributes)
        for i in range(len(job_attributes)):
            job[x][i].append(job_attributes)
        x = x + 1
        line = job_file.readline()


if __name__ == "__main__":
    readfile()