def inner_generator():
    i = 0
    while True:
        print("inner")
        i = yield i
        if i > 10:
            raise StopIteration


def outer_generator():
    print("do something before coroutine start")
    yield from inner_generator()


def main():
    g = outer_generator()
    g.send(None)
    i = 0
    while 1:
        try:
            i = g.send(i + 1)
            print(i)
        except StopIteration:
            break

if __name__ == '__main__':
    main()



# def inner_generator():
#     i = 0
#     while True:
#         print("inner")
#         i = yield i
#         if i > 10:
#             raise StopIteration
#
#
#
# def outer_generator():
#     print("do something before yield")
#     from_inner = 0
#     from_outer = 1
#     g = inner_generator()
#     g.send(None)
#     while 1:
#         try:
#             print('outer')
#             from_inner = g.send(from_outer)
#             # print("from_inner",from_inner)
#             from_outer = yield from_inner
#             # print("from_outer", from_outer)
#         except StopIteration:
#             break
#
#
# def main():
#     g = outer_generator()
#     g.send(None)
#     i = 0
#     while 1:
#         try:
#             print('main')
#             i = g.send(i + 1)
#             print(i)
#         except StopIteration:
#             break
#
#
# if __name__ == '__main__':
#     main()
#
#
