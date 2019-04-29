

def readfile():
    job_file = open("jobs.dat", "r")
    jobs = []
    line = job_file.readline()
    while line:
        line = line.split()
        jobs.append(Job(int(line[0]), int(line[1]), int(line[2])))
        line = job_file.readline()
    return jobs


def fifo(jobs):

    i = 0
    time = 0
    while i < len(jobs):
        job = jobs[i]
        job.start = time
        job.completion = time + job.duration
        time = time + job.duration
        i += 1

        # TODO calc turn around and response time
        #

    test = 1



def sjf(jobs):
 ''' i=0
    time = 0
    job= jobs[i]
   job.sort(key=lambda job:job.arrival_time )
for j in range(1, len(processes)):
         ab = pro[j-1].ct

         # partial sorting  <-------------- right here !!!!
         waitings = list(filter(lambda x: x.at <= ab, pro[j:]))
         pro[j:j+len(waitings)] = sorted(waitings, key=lambda x: x.bt)
         # partial sorting end

         if pro[j-1].ct < pro[j].at:
             pro[j].ct = pro[j-1].ct + pro[j].bt + pro[j].at - pro[j-1].ct
         else:
             pro[j].ct = pro[j-1].ct + pro[j].bt

'''


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

    def __repr__(self):
        return "job_id: {}, arrival_time: {},duration: {}".format(self.job_id,self.arrival_time,self.duration)

if __name__ == "__main__":
    jobs = readfile()
    fifo(jobs)
    print(jobs[1])
    print(jobs[0])