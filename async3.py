import asyncio
import time


now = lambda :time.time()
async def do_some_work(x):
    print('Waiting:',x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(2)

tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]
start = now()
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt as e:
    print(asyncio.Task.all_tasks())
    for task in asyncio.Task.all_tasks():
        print(task.cancel())
    loop.stop()
    loop.run_forever()
finally:
    loop.close()
print('TIME:',now()-start)

#
# now = lambda :time.time()
# async def do_some_work(x):
#     print('Waiting: ',x)
#     await asyncio.sleep(x)
#     return 'Done after {}s'.format(x)
#
# start = now()
#
# coroutine1 = do_some_work(1)
# coroutine2 = do_some_work(2)
# coroutine3 = do_some_work(4)
#
# tasks = [
#     asyncio.ensure_future(coroutine1),
#     asyncio.ensure_future(coroutine2),
#     asyncio.ensure_future(coroutine3)
# ]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
#
# for task in tasks:
#     print('Task ret:', task.result())
# print('TIME:',now()-start)

# async def do_some_work(x):
#     print("Waiting: ",x)
#     await  asyncio.sleep(x)
#     return 'Done after {}s'.format(x)
#
# start = now()
# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# loop.run_until_complete(task)
# print('Task ret: ',task.result())
# print('TIME: ',now()-start)


# now = lambda :time.time()
# async def do_some_work(x):
#     print('Waiting {}'.format(x))
#     return 'Done after {}s'.format(x)
#
# start = now()
# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# loop.run_until_complete(task)
# print('Task ret: {}'.format(task.result()))
# print('Time:{}'.format(now()-start))


# now = lambda :time.time()
# async def do_some_work(x):
#     print('Waiting:', x)
#     return 'Done after {}s'.format(x)
#
# def callback(future):
#     print('Callback: ', future.result())
#
# start = now()
# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# task.add_done_callback(callback)
# loop.run_until_complete(task)
# print('TIME:', now()-start)



# now = lambda :time.time()
# async def do_some_work(x):
#     print('Waiting:',x)
#
# start = now()
# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
#
# task = loop.create_task(coroutine)
# print(task)
#
# loop.run_until_complete(task)
# print(task)
# print('Time:', now()-start)










# import time
# import asyncio
#
# now = lambda :time.time()
#
# async def do_some_work(x):
#     print('Waiting:', x)
#
# start = now()
# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)
# print('TIME:', now()-start)