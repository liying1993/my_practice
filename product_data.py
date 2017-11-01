from collections import defaultdict

network = defaultdict(list)
def make_dict(my_dict):
    for key in my_dict:
        network[key[0]].append(key[1])
        network[key[1]].append(key[0])
    return network

if __name__ == '__main__':
    my_dict = [[0,1],[1,2],[1,4],[2,3],[4,5],[4,6]]
    result = make_dict(my_dict)
    print(result)


