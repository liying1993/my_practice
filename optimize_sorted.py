def sortby(somelist, n):
    import pdb
    pdb.set_trace()
    nlist = [(x[n], x) for x in somelist]
    nlist.sort()
    print("-------")
    print(nlist)
    return [val for (key, val) in nlist]

def sorted_inplace(somelist, n):
    somelist[:] = [(x[n],x) for x in somelist]
    # print(somelist)
    somelist.sort()
    somelist[:] = [val for (key, val) in somelist]
    return
if __name__ == "__main__":
    somelist = [(1, 2, 'def'), (2, -4, 'ghi'), (3, 6, 'abc')]
    somelist.sort()
    print(somelist)
    nlist = sortby(somelist, 2)
    # tlist = sorted_inplace(somelist, 2)
    print(nlist)
    # print(tlist)