import requests
import scrapy
from bs4 import BeautifulSoup
'''
使用requests,scrapy,bs4,还有gevent写一个简单的爬虫，爬取花椒主播的图片
'''

def scrapy_huajiao(url):
    result = requests.get(url)
    print(result.text)








if __name__ == "__main__":
    urls = ["http://www.huajiao.com/l/152195707", "http://www.huajiao.com/l/152208467"]
    scrapy_huajiao(urls[0])










# class gwhatweb(object):
#     def __init__(self, url):
#         self.tasks = Queue()
#         self.url = url.rstrip("/")
#         fp = open("data.json")
#         # fp = fp.decode("US-ASCII")
#         import pdb
#         # pdb.set_trace()
#         print(type(fp))
#         webdata = json.load(fp)
#         for i in webdata:
#             self.tasks.put(i)
#         fp.close()
#         print("webdata total:%d" %len(webdata))
#
#     def _GetMd5(self, body):
#         m2 = hashlib.md5()
#         m2.update(body)
#         return m2.hexdigest()
#
#     def _clearQueue(self):
#         while not self.tasks.empty():
#             self.tasks.get()
#
#     def _worker(self):
#         data = self.tasks.get()
#         test_url = self.url + data["url"]
#         rtext = ''
#         try:
#             r = requests.get(test_url, timeout=10)
#             if (r.status_code != 200):
#                 return
#             rtext = r.text
#             if rtext is None:
#                 return
#         except:
#             rtext = ''
#
#         if data["re"]:
#             if (rtext.find(data["re"]) != -1):
#                 result = data["name"]
#                 print("CMS:%s Judge:%s re:%s" %(result, test_url, data["re"]))
#                 self._clearQueue()
#                 return True
#         else:
#             md5 = self._GetMd5(rtext)
#             if (md5 == data["md5"]):
#                 result = data["name"]
#                 print("CMS:%s Judge:%s md5:%s" %(result, test_url, data["md5"]))
#                 self._clearQueue()
#                 return True
#
#     def _boss(self):
#         while not self.tasks.empty():
#             self._worker()
#
#
#     def whatweb(self, maxsize=100):
#         start = time.clock()
#         allr = [gevent.spawn(self._boss) for i in range(maxsize)]
#         gevent.joinall(allr)
#         end = time.clock()
#         print("cost: %f s" %(end-start))
#
# if __name__ == "__main__":
#     print(sys.argv[1])
#     if len(sys.argv) < 2:
#         print("usag:python gwhatweb.py http://www.xxx.com")
#     else:
#         url = sys.argv[1]
#         g = gwhatweb(url)
#         g.whatweb(1000)







# pool = Pool(2)
#
# def hello_from(n):
#     print('Size of pool %s'% len(pool))
# pool.map(hello_from, range(3))



# def talk(msg):
#     for i in range(2):
#         print(msg)
#
#
# g1 = gevent.spawn(talk, 'bar')
# g2 = gevent.spawn(talk, 'foo')
# g3 = gevent.spawn(talk, 'fizz')
#
# group = Group()
# group.add(g1)
# group.add(g2)
# group.join()
#
# group.add(g3)
# group.join()



# tasks = Queue()
#
# def worker(n):
#     while not tasks.empty():
#         task = tasks.get()
#         print('Worker %s got task %s' % (n, task))
#         gevent.sleep(0)
#     print('Quintting time!')
#
# def boss():
#     for i in range(1,10):
#         tasks.put_nowait(i)
#
# gevent.spawn(boss).join()
#
# gevent.joinall([
#     gevent.spawn(worker, 'steve'),
#     gevent.spawn(worker, 'join'),
#     gevent.spawn(worker, 'nancy'),
# ])






# a = AsyncResult()
#
# def setter():
#     gevent.sleep(3)
#     a.set('Hello!')
#
# def waiter():
#     print(a.get())
#
# gevent.joinall([
#     gevent.spawn(setter),
#     gevent.spawn(waiter),
# ])

# evt = Event()
#
# def setter():
#     print('A:Hey wait for me ,I have to do something')
#     gevent.sleep(3)
#     print('OK, I am done')
#     print(evt.set())
#     evt.set()
#
# def waiter():
#     print('I will wait for you')
#     evt.wait()
#     print("It is about time")
#
# def main():
#     gevent.joinall([
#         gevent.spawn(setter),
#         gevent.spawn(waiter),
#         gevent.spawn(waiter),
#         gevent.spawn(waiter)
#     ])
#
# if __name__  == "__main__":
#     main()






#
# print(socket.socket)
#
# print('After monkey patch')
# monkey.patch_socket()
# print(socket.socket)
#
#
# print(select.select)
# monkey.patch_select()
# print('After monkey patch')
# print(select.select)










# time_to_wait = 5
# class TooLong(Exception):
#     pass
#
# with Timeout(time_to_wait, TooLong):
#     gevent.sleep(10)









# seconds = 10
# timeout = Timeout(seconds)
# timeout.start()
#
#
# def wait():
#     gevent.sleep(10)
#
# try:
#     gevent.spawn(wait).join()
# except Timeout:
#     print('Could not complete')






# def run_forever():
#     gevent.sleep(1000)
#
# if __name__ == "__main__":
#     gevent.signal(signal.SIGQUIT, gevent.shutdown)
#     thread = gevent.spawn(run_forever)
#     thread.join()








# class MyGreenlet(Greenlet):
#
#     def __init__(self, message, n):
#         Greenlet.__init__(self)
#         self.message = message
#         self.n = n
#
#     def _run(self):
#         print(self.message)
#         gevent.sleep(self.n)
#
# g = MyGreenlet("Hi there!", 3)
# g.start()
# g.join()
# print(g.value())





# def foo(message, n):
#     gevent.sleep(n)
#     print(message)
#
# thread1 = Greenlet.spawn(foo, "Hello", 1)
# thread2 = gevent.spawn(foo, "I live!", 2)
# thread3 = gevent.spawn(lambda x: (x+1), 2)
# threads = [thread1, thread2, thread3]
# gevent.joinall(threads)


# def echo(i):
#     time.sleep(0.001)
#     return i
# from multiprocessing.pool import Pool
# p = Pool(10)
#
# run1 = [a for a in p.imap_unordered(echo, range(10))]
# run2 = [a for a in p.imap_unordered(echo, range(10))]
# run3 = [a for a in p.imap_unordered(echo, range(10))]
# run4 = [a for a in p.imap_unordered(echo, range(10))]
#
# print(run1 == run2 == run3 ==run4)
#
# from gevent.pool import Pool
#
# p = Pool(10)
# run1 = [a for a in p.imap_unordered(echo, range(10))]
# run2 = [a for a in p.imap_unordered(echo, range(10))]
# run3 = [a for a in p.imap_unordered(echo, range(10))]
# run4 = [a for a in p.imap_unordered(echo, range(10))]
#
#
# print(run1 == run2 == run3 == run4)
#





# def task(pid):
#     gevent.sleep(random.randint(0,2)*0.001)
#     print('Task %s done' %pid)
#
# def synchronous():
#     for i in range(5):
#         task(i)
#
# def asynchronous():
#     threads = [gevent.spawn(task, i) for i in range(5)]
#     gevent.joinall(threads)
#
#     print('Synchronous:')
#     synchronous()
#
#     print('Asynchronous')
#     asynchronous()










#
# start = time.time()
# tic = lambda: 'at %1.1f seconds' %(time.time() - start)
#
# def gr1():
#     print("Started Polling：%s" %  tic())
#     select.select([],[],[],1)
#     print('Enabled Polhttp://jp.tingroom.com/ling:%s' %tic())
#
# def gr2():
#     print('started polling:%s' %tic())
#     select.select([],[],[],2)
#     print('Enabled polling:%s'%tic())
#
# def gr3():
#     print("Hey lets do")
#     gevent.sleep(1)
#
# gevent.joinall([
#     gevent.spawn(gr1),
#     gevent.spawn(gr2),
#     gevent.spawn(gr3),
# ])


















#======================================解释协程的工作特性，首先执行foo，然后foo sleep,停止foo取执行bar,然后bar停止foo被释放，再去执行foo
# def foo():
#     print("Running in foo")
#     gevent.sleep(0)
#     print("Explicit context switch to foo again")
#
#
# def bar():
#     print("Explicit context to bar")
#     gevent.sleep(0)
#     print("Implicit context switch back to bar")
#
# gevent.joinall([
#     gevent.spawn(foo),
#     gevent.spawn(bar),
# ])
