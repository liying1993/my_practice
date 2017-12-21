


#
# import queue
#
# def task(name, queue):
#     while not queue.empty():
#         count = queue.get()
#         print("====count===",count)
#         total = 0
#         for x in range(count):
#             print(f'Task {name} running {x}')
#             total += 1
#             yield
#         print(f'Task {name} total: {total}')
#
#
# def main():
#     work_queue = queue.Queue()
#     for work in [15,10,5,2]:
#         work_queue.put(work)
#     tasks = [
#         task('One', work_queue),
#         task('Two', work_queue)
#     ]
#     print(tasks)
#     done = False
#     while not done:
#         for t in tasks:
#             try:
#                 print("tasking")
#                 next(t)
#                 print("======task=====",t)
#             except StopIteration:
#                 tasks.remove(t)
#             if len(tasks) == 0:
#                 done = True
#
# if __name__ == '__main__':
#     main()






# import queue
#
# def task(name, work_queue):
#     if work_queue.empty():
#         print(f'Task {name} nothing th do')
#     else:
#         while not work_queue.empty():
#             count = work_queue.get()
#             total = 0
#             for x in range(count):
#                 print(f'Task {name} running')
#                 total += 1
#             print(f'Task {name} total: {total}')
#
# def main():
#     work_queue = queue.Queue()
#     for work in [15, 10, 5, 2]:
#         work_queue.put(work)
#     tasks = [
#         (task, 'One', work_queue),
#         (task, 'Two', work_queue)
#     ]
#     for t, n, q in tasks:
#         t(n,q)
# if __name__ == '__main__':
#     main()