import sys


if __name__ == '__main__':
    total = int(sys.stdin.readline().strip())
    src = []
    for line in sys.stdin.readlines():
        i_ = int(line.strip())
        if i_ in src:
            continue
        else:
            src.append(i_)
    src.sort()
    for i in src:
        sys.stdout.write(f"{src}\n")
