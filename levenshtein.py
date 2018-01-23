import numpy as np

def func(str_a, str_b):
    length = max(len(str_a), len(str_b))
    origin_arr = np.zeros((length,length), dtype=int)
    indexi = 0
    indexj = 0
    for i,valuei in enumerate(origin_arr):
        for j, valuej in enumerate(origin_arr[i]):
            if i == 0:
                valuei[j] = indexj
                indexj += 1
            if j == 0:
                valuei[0] = indexi
                indexi += 1
    return origin_arr

def levelshtein(arr):
    length = np.shape(arr)[0] - 1
    for i in range(length):
        for j in range(length):
            x,y = i+1, j+1
            try:
                if str_b[x] == str_a[y]:
                    arr[x][y] = min(arr[x-1, y]+1,arr[x-1, y-1], arr[x, y-1]+1)
                else:
                    arr[x][y] = min(arr[x-1,y]+1, arr[x-1][y-1]+1, arr[x, y-1]+1)
            except Exception:
                arr[x][y] = min(arr[x - 1, y] + 1, arr[x - 1][y - 1] + 1, arr[x, y - 1] + 1)

    return arr[length][length]


if __name__ == '__main__':
    str_a = "lla"
    str_b = "lalalala"
    arr = func(str_a, str_b)
    result = levelshtein(arr)
    print(result)