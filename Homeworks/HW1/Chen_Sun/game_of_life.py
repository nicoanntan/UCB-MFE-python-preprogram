import numpy as np
import copy

def evolve(initial_state):
    rownumber = len(initial_state)
    colnumber = len(initial_state[0])
    nliving = 0
    newlife = []
    for i in range (rownumber):
        newlife_row = [x for x in range(rownumber)]
        newlife.append(newlife_row)
    for i in range (rownumber):
        for j in range (colnumber):
            if i == 0 and j == 0:
                nliving = initial_state[i+1][j]+initial_state[i][j+1]+initial_state[i+1][j+1]
            elif i == 0 and j == colnumber - 1:
                nliving = initial_state[i+1][j]+initial_state[i][j-1]+initial_state[i+1][j-1]
            elif i == rownumber - 1 and j == 0:
                nliving = initial_state[i][j+1]+initial_state[i-1][j]+initial_state[i-1][j+1]
            elif i == rownumber - 1 and j == colnumber - 1:
                nliving = initial_state[i-1][j]+initial_state[i][j-1]+initial_state[i-1][j-1]
            elif i == 0 and 0< j <colnumber - 1:
                nliving = initial_state[i][j-1]+initial_state[i+1][j-1]+initial_state[i+1][j]+initial_state[i+1][j+1]+initial_state[i][j+1]
            elif i == rownumber - 1 and 0<j<colnumber - 1:
                nliving = initial_state[i][j-1]+initial_state[i-1][j-1]+initial_state[i-1][j]+initial_state[i-1][j+1]+initial_state[i][j+1]
            elif 0<i<rownumber - 1 and j == 0:
                nliving = initial_state[i-1][j]+initial_state[i-1][j+1]+initial_state[i][j+1]+initial_state[i+1][j+1]+initial_state[i+1][j]
            elif 0<i<rownumber - 1 and j == colnumber - 1:
                nliving = initial_state[i-1][j]+initial_state[i-1][j-1]+initial_state[i][j-1]+initial_state[i+1][j-1]+initial_state[i+1][j]
            else:
                nliving = initial_state[i-1][j-1]+initial_state[i-1][j]+initial_state[i-1][j+1]+initial_state[i][j-1]+initial_state[i][j+1]+initial_state[i+1][j-1]+initial_state[i+1][j]+initial_state[i+1][j+1]
                
            if initial_state[i][j] == 1 and nliving < 2:
                newlife[i][j] = 0
            elif initial_state[i][j] == 1 and nliving == 2:
                newlife[i][j] = 1
            elif initial_state[i][j] == 1 and nliving == 3:
                newlife[i][j] = 1
            elif initial_state[i][j] == 1 and nliving > 3:
                newlife[i][j] = 0
            elif initial_state[i][j] == 0 and nliving == 3:
                newlife[i][j] = 1
            else:
                newlife[i][j] = 0
    return newlife

    pass  
            
test_case_1 = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
]


test_case_2 = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]


test_case_2_next = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


assert evolve(test_case_1) == test_case_1
assert evolve(test_case_2) == test_case_2_next
