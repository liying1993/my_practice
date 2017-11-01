from collections import defaultdict

network = defaultdict(list)


def make_dict(my_dict):
    for key in my_dict:
        network[key[0]].append(key[1])
        network[key[1]].append(key[0])
    return network


def max_depth(parent, node):
    # if leaf node
    depth = 0

    if len(network[node]) == 1:
        return 0

    for child in network[node]:
        if parent == child:
            continue
        depth = max(depth, 1 + max_depth(node, child))

    return depth


def get_final_depth():
    for key, value in network.items():
        # depth_list = []
        result = (1 + max_depth(key, i) for i in network[key])
        for i in network[key]:
            m_d = 1 + max_depth(key, i)
            yield m_d
            # depth_list.append(m_d)
            #     final_depth.append(max(depth_list))
            # print(min(final_depth))


if __name__ == '__main__':
    my_dict = [[0, 1], [1, 2], [1, 4], [2, 3], [4, 5], [4, 6]]
    final_depth = []
    result = make_dict(my_dict)
    print(result)
    aa = [1 + max_depth(key, value) for key, value in network.items() for value in network[key]]
    for key, value in network.items():
        depth_list = []
        for i in network[key]:
            m_d = 1 + max_depth(key, i)
            depth_list.append(m_d)
        print(depth_list)
        final_depth.append(max(depth_list))
    print(final_depth)
    print(min(final_depth))













    # n = int(input())  # the number of adjacency relations
    # network = defaultdict(list)
    # final_depth = []
    # for i in range(n):
    #     # xi: the ID of a person which is adjacent to yi
    #     # yi: the ID of a person which is adjacent to xi
    #     xi, yi = [int(j) for j in input().split()]
    #     network[xi].append(yi)
    #     network[yi].append(xi)
    #
    #
    # # print(network)
    #
    #
    # def max_depth(parent, node):
    #     # if leaf node
    #     if len(network[node]) == 1:
    #         return 0
    #
    #     depth = 0
    #
    #     for child in network[node]:
    #         if parent == child:
    #             continue
    #         depth = max(depth, 1 + max_depth(node, child))
    #
    #     return depth
    #
    #
    # # m_d = [max_depth(key, value) for key, value in network.items()]
    # for key, value in network.items():
    #     depth_list = []
    #     for i in network[key]:
    #         m_d = 1 + max_depth(key, i)
    #         depth_list.append(m_d)
    #     final_depth.append(max(depth_list))
    #
    # print(min(final_depth))
