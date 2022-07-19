import sys


if __name__ == '__main__':

    string = sys.stdin.readline()
    chr_ = sys.stdin.readline().strip().lower()
    cnt = 0

    for c in string:
        if c.lower() == chr_:
            cnt += 1
    print(cnt)