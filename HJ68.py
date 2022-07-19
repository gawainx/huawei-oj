import sys

if __name__ == '__main__':
    cnt = int(sys.stdin.readline().strip())
    reverse = bool(int(sys.stdin.readline().strip()))

    src = []
    for line in sys.stdin.readlines():
        a = line.strip().split()
        name, score = a[0], int(a[1])
        src.append((name, score))
    src.sort(key=lambda x: x[1], reverse=reverse)
    for name, score in src:
        sys.stdout.write(f"{name} {score}\n")