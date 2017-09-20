import time, os
import threading
from queue import Queue
import pdb

th_lock = threading.Lock()
class WorkerThread(threading.Thread):
    def __init__(self, dir_q, result_q):
        super(WorkerThread, self).__init__()
        self.dir_q = dir_q
        self.result_q = result_q
        self.stoprequest = threading.Event()
    def run(self):
        # pdb.set_trace()
        while not self.stoprequest.isSet():
            try:
                # print("zhejiushiceshi")
                th_lock.acquire()
                dirname = self.dir_q.get(True, 0.05)
                # print(dirname)
                filenames = list(self._files_in_dir(dirname))
                # print(filenames)
                self.result_q.put((self.name, dirname, filenames))
                print(threading.current_thread().name)
                print(self.result_q)
                th_lock.release()
            except Exception:
                continue

    def join(self, timeout = None):
        # pdb.set_trace()
        self.stoprequest.set()
        super(WorkerThread, self).join(timeout)

    def _files_in_dir(self, dirname):
        # pdb.set_trace()
        for path, dirs, files in os.walk(dirname):
            for file in files:
                yield  os.path.join(path, file)

def main(args):

    # pdb.set_trace()
    dir_q = Queue()
    result_q = Queue()
    pool = [WorkerThread(dir_q=dir_q, result_q=result_q) for i in range(4)]
    for thread in pool:
        # print("before ceshi")
        thread.start()
    work_count = 0
    for dir in args:
        if os.path.exists(dir):
            work_count += 1
            dir_q.put(dir)
    print('Assigned %s dirs to workders'%work_count)

    while work_count >0 :
        result = result_q.get()
        print('From thread %s:%s files found in dir %s'%(result[0], len(result[2]), result[1]))
        work_count -= 1
    for thread in pool:
        print("lalalalal")
        thread.join()

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])