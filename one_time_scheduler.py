import time
import threading
import schedule
import datetime

class OneTimeScheduler:
    __lock = threading.Lock()
    __jobs = dict()
    __never_jobs = dict()
    __sequence = 1

    def __job(self, seq, job):
        self.__lock.acquire()
        schedule.cancel_job(self.__jobs.pop(seq))
        self.__lock.release()
        job()
    
    def __loop(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
    
    def cancel(self, job_id):
        self.__lock.acquire()
        schedule.cancel_job(self.__jobs.pop(job_id))
        self.__lock.release()
    
    def never_hour(self, hour, job):
        actural = schedule.every().day.at(self.__create_time_string(hour)).do(lambda : self.__never_hour_job(hour, job))
        self.__never_jobs[job] = actural
    
    def __never_hour_job(self, hour, job):
        schedule.cancel_job(self.__never_jobs.pop(job))
        job()
        self.never_hour(hour, job)

    def __create_time_string(self, hour):
        now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+9)))
        next_hour = now + datetime.timedelta(hours=hour)
        if next_hour.hour > 9:
            return str(next_hour.hour) + ':00'
        else:
            return '0' + str(next_hour.hour) + ':00'
    
    def after_minutes(self, minutes, job, job_id=None):
        self.__lock.acquire()
        seq = self.__sequence
        if job_id == None:
            self.__sequence += 1
        else:
            seq = job_id
        self.__jobs[seq] = schedule.every(minutes).minutes.do(lambda : self.__job(seq, job))
        self.__lock.release()
        return seq

    def run(self):
        self.thread = threading.Thread(target=self.__loop, daemon=True)
        self.thread.start()