import numpy as np


def get_next_coordinate(matrix, dir,  x, y):
    change_dir = None
    if dir == 'R':
        if matrix[x][y+1] != 0:
            x = x + 1
            change_dir = False
        else:
            y = y+1
            change_dir = True
    elif dir == 'U':
        if matrix[x-1][y] != 0:
            y = y + 1
            change_dir = False
        else:
            x = x - 1
            change_dir = True
    elif dir == 'L':
        if matrix[x][y-1] != 0:
            x = x - 1
            change_dir = False
        else:
            y = y - 1
            change_dir = True
    elif dir == 'D':
        if matrix[x+1][y] != 0:
            y = y - 1
            change_dir = False
        else:
            x = x+1
            change_dir = True
    return x,y,change_dir


def get_value(matrix, x, y):
    numrows = len(matrix)    # 3 rows in your example
    numcols = len(matrix[0])
    value = 0
    if x - 1 > 0:
        value += int(matrix[x-1][y])
    if x - 1 > 0 and  y - 1 >0:
        value += int(matrix[x-1][y-1])
    if y - 1 > 0:
        value += int(matrix[x][y-1])
    if x + 1 < numrows and y - 1 > 0:
        value += int(matrix[x+1][y - 1])
    if x + 1 < numrows :
        value += int(matrix[x+1][y])
    if x + 1 < numrows and y + 1 < numcols:
        value += int(matrix[x+1][y+1])
    if y + 1 < numcols:
        value += int(matrix[x][y+1])
    if x - 1 > 0 and y + 1 < numcols:
        value += int(matrix[x-1][y+1])

    if value == 0:
        return 1
    return value



def main():
    matrix = [[0 for i in range(11)] for j in range(11)]
    dir = ['D', 'L', 'U', 'R']
    x, y = 5, 5

    while 11 > x >= 0 and 11 > y >= 0:
        matrix[x][y] = get_value(matrix ,x, y)
        if matrix[x][y] >= 361527:
            print("Found it!!" + str(matrix[x][y]))
            break

        cur_dir = dir[3]
        x, y, chng_dir = get_next_coordinate(matrix, cur_dir, x, y)
        if chng_dir:
            cur_dir = dir.pop()
            dir.insert(0, cur_dir)

    print(np.matrix(matrix))


main()
