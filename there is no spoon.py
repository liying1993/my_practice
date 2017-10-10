array_list = [['0', '0'], ['0', '.']]
for index, value in enumerate(array_list):
    # print(index, value)
    for in_index, in_value in enumerate(value):
        # print(in_index, in_value)
        if array_list[index][in_index + 1] == ".":
            print(array_list[index][in_index],-1,-1,array_list[index+1][in_index])
        elif array_list[index + 1][in_index] == ".":
            print(array_list[index][in_index],array_list[index][in_index + 1],-1,-1)
        elif array_list[index][in_index + 1] == "." or array_list[index + 1][in_index] == ".":
            print()
        else:
            print(array_list[index][in_index],array_list[index][in_index + 1],array_list[index+1][in_index])
