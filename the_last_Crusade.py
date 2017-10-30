import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
rooms = []
MAP_RULES = {
    '0':{},
    '1':{'LEFT':'BOTTOM', 'TOP':'BOTTOM', 'RIGHT':'BOTTOM'},
    '2':{'LEFT':'RIGHT', 'RIGHT':'LEFT'},
    '3':{'TOP': 'BOTTOM'},
    '4':{'TOP':'LEFT', 'RIGHT': 'BOTTOM'},
    '5':{'TOP':'RIGHT', 'LEFT': 'BOTTOM'},
    '6':{'LEFT':'RIGHT', 'RIGHT':'LEFT'},
    '7':{'TOP':'BOTTOM', 'RIGHT':'BOTTOM'},
    '8':{'LEFT':'BOTTOM', 'RIGHT':'BOTTOM'},
    '9':{'LEFT':'BOTTOM', 'TOP': 'BOTTOM'},
    '10':{'TOP':'LEFT'},
    '11':{'TOP':'RIGHT'},
    '12':{'RIGHT':'BOTTOM'},
    '13':{'LEFT':'BOTTOM'},
}
# print(w,h)#(3,3)
for i in range(h):
    rooms.append(input().split())  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
#     print(line)
# print(rooms)#['0 3 0', '0 3 0', '0 3 0']
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).
# print(ex)#1

# game loop
while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)
    # print(xi, yi)
    room_now = rooms[yi][xi]
    next_pos = MAP_RULES[room_now][pos]
    if next_pos == "BOTTOM":
        xi_next = xi
        yi_next = yi+1
    elif next_pos == "LEFT":
        xi_next = xi-1
        yi_next = yi
    elif next_pos == "RIGHT":
        xi_next = xi+1
        yi_next = yi
    print(xi_next, yi_next)
#my code
