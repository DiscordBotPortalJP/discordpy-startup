import time
import threading
import schedule
import datetime
import asyncio

class OneTimeScheduler:
    __lock = threading.Lock()
    __jobs = dict()
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
    
    def never_hour(self, job):
        schedule.every().hour.at(":00").do(job)

    def never_wednesday(self, at, job):
        schedule.every().wednesday.at(at).do(job)
    
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

    def run_thread(self):
        self.thread = threading.Thread(target=self.__loop, daemon=True)
        self.thread.start()
    
    async def __loop_asyncio(self, loop):
        schedule.run_pending()
        await asyncio.sleep(1, loop=loop)
        asyncio.ensure_future(self.__loop_asyncio(loop), loop=loop)

    def run_asyncio(self, loop):
        asyncio.ensure_future(self.__loop_asyncio(loop), loop=loop)