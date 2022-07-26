"""
迷宫问题

- 要读入数组
- 广度优先搜索？
- 感觉可以用回溯来进行的

错误点：
- 可以往上走
- 可是往上走的同时不能走回头路
"""
import sys

if __name__ == '__main__':
    nm = input().strip().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    line = input()
    while len(line) != 0:
        line = line.strip().split()
        arr.append([int(a) for a in line])
        if len(arr) == n:
            break
        line = input()
    stk = [[(0, 0)]]
    res_path = None
    while len(stk) != 0:
        last_path = stk.pop()
        x, y = last_path[-1]
        if x == n - 1 and y == m - 1:
            res_path = last_path[:]
            break
        if len(last_path) == 1:
            # start node
            if arr[x + 1][y] == 0:
                stk.append(last_path + [(x + 1, y)])
            if arr[x][y + 1] == 0:
                stk.append(last_path + [(x, y + 1)])
        else:
            prev_x, prev_y = last_path[-2]
            if prev_x < x:
                # check left, right and down
                if y > 0 and arr[x][y - 1] == 0 and (x, y - 1) not in last_path:
                    # left
                    stk.append(last_path + [(x, y - 1)])
                if y < m - 1 and arr[x][y + 1] == 0 and (x, y + 1) not in last_path:
                    stk.append(last_path + [(x, y + 1)])
                if x < n - 1 and arr[x + 1][y] == 0 and (x + 1, y) not in last_path:
                    stk.append(last_path + [(x + 1, y)])
            elif prev_x == x:
                # up, down, and right
                if x > 0 and arr[x - 1][y] == 0 and (x - 1, y) not in last_path:
                    # up
                    stk.append(last_path + [(x - 1, y)])
                if x < n - 1 and arr[x + 1][y] == 0 and (x + 1, y) not in last_path:
                    # down
                    stk.append(last_path + [(x + 1, y)])
                if prev_y < y < m - 1 and arr[x][y + 1] == 0 and (x, y + 1) not in last_path:
                    # right
                    stk.append(last_path + [(x, y + 1)])
                if 0 < y < prev_y and arr[x][y - 1] == 0 and (x, y - 1) not in last_path:
                    # left
                    stk.append(last_path + [(x, y - 1)])

            else:
                # prev_x > x
                # left, right and up
                if x > 0 and arr[x - 1][y] == 0 and (x - 1, y) not in last_path:
                    stk.append(last_path + [(x - 1, y)])
                if y > 0 and arr[x][y - 1] == 0 and (x, y - 1) not in last_path:
                    stk.append(last_path + [(x, y - 1)])
                if y < m - 1 and arr[x][y + 1] == 0 and (x, y + 1) not in last_path:
                    stk.append(last_path + [(x, y + 1)])
    for x, y in res_path:
        sys.stdout.write(f"({x},{y})\n")
