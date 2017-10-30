from collections import defaultdict


network = defaultdict(list)
def max_depth(parent, node):
    # if leaf node
    if len(network[node]) == 1:
        return 0

    depth = 0

    for child in network[node]:
        if parent == child:
            continue
        depth = max(depth, 1 + max_depth(node, child))

    return depth


# m_d = [max_depth(key, value) for key, value in network.items()]
for key, value in network.items():
    for i in network[key]:
        m_d = max_depth(key, i)

