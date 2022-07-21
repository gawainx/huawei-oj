"""动态规划试水"""

import sys

if __name__ == '__main__':
    nm = sys.stdin.readline().strip().split()
    n, m = int(nm[0]), int(nm[1])
    arr = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    arr[0][0] = 0
    arr[0][1] = arr[1][0] = 1
    arr[1][1] = 2
    for j in range(1, m + 1):
        arr[0][j] = 1
    for i in range(1, n + 1):
        arr[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

    print(arr[n][m])
