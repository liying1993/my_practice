from functools import wraps

def memo(f):
    import pdb
    # pdb.set_trace()
    cache = {}
    @wraps(f)
    def wrap(*arg):
        import pdb
        pdb.set_trace()
        if arg not in cache:cache['arg'] = f(*arg)
        return cache['arg']
    return wrap

# @memo
def fib(i):
    import pdb
    # pdb.set_trace()
    if i<2: return i
    return fib(i-1)+fib(i-2)

def wrap_time(f):
    @wraps(f)
    def wrap(*args):
        import time
        start_time = time.time()
        print("lalla")
        end_time = time.time()
        print("this is the end")
        cha = end_time-start_time
        print(cha)
        return cha
    return wrap

@wrap_time
def my_time():
    print("my_time")




if __name__ == "__main__":
    my_time()
