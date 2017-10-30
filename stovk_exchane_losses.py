
# import operator
#
# result = []
# origin_num = [3, 4, 7, 9, 10]
# for i, value in enumerate(origin_num):
#     param_right = origin_num[i + 1:]
#     if len(param_right) != 0:
#         param_left = [value] * len(param_right)
#         max_distance = max(list(map(operator.sub, param_left, param_right)))
#         if max_distance > 0:
#             result.append(max_distance)
# if len(result) == 0:
#     print(0)
# else:
#     print(-max(result))



# n = int(input())
prices = map(int, ["3", "2", "4", "2", "1", "5"])
print(prices)

loss = 0
high = next(prices)

for p in prices:
    high = max(high, p)
    loss = min(loss, p - high)

print(loss)