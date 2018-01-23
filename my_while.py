import bisect
my_list = [1, 1, 1, 2, 3, 4, 5, 8, 10, 22, 24, 25, 26, 66]
my_set_list = sorted(list(set(my_list)))
i=0
c = []
d = []
try:
    while True:
       if my_set_list[i]+1 in my_list:
           c.append(my_set_list[i]+1)
       else:
           if len(c):
               la = c[0]-1
               c.append(la)
               e = sorted(c)
               # e = sorted(c.append((c[0]-1)))
               d.append(e)
               c = []
           else:
               d.append(my_set_list[i])
       i = i+1
except Exception as e:
    pass
    print(e)
    # d.append(my_set_list[i])
