import sys

if __name__ == '__main__':
    _ = sys.stdin.readline()
    res = []
    for x in range(0, 101):
        for y in range(0, 101):
            if x + y > 100:
                continue
            else:
                z = 100 - (x + y)
                if 5 * x + 3 * y + (1/3)*z == 100:
                    if (x, y, z) not in res:
                        res.append((x, y, z))
    for x, y, z in res:
        sys.stdout.write(f"{x} {y} {z}\n")
