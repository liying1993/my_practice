# data = {}
# cnt = 0
# telephones = {"12", "12234567", "256", "12543"}
# for telephone in telephones:
#     print(telephone)
#     temp = data
#     for t in telephone:
#         val = temp.get(t, None)
#         if val == None:
#             cnt += 1
#         temp = temp.setdefault(t, {})
# print(cnt)

contest_data = {"12", "12234567", "256", "12543"}
telephones = set()
for s in contest_data:
    # for i in range(len(s)):
    #     telephones.update(set(s[0:i+1]))
    telephones.update(set(s[0:i + 1] for i in range(len(s))))
print(len(telephones))

# for i in range(int(input())):
#     s = input()
#     telephones.update(set(s[0:i+1] for i in range(len(s))))
# print(len(telephones))