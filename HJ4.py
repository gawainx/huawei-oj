import sys

if __name__ == '__main__':
    src = sys.stdin.readline().strip()
    if len(src) < 8:
        s_ = src + '0' * (8 - len(src))
        sys.stdout.write(s_)
        sys.stdout.write('\n')
    else:
        res = []
        ln = len(src)
        for i in range(0, ln, 8):
            s_ = src[i: i + 8]
            if i + 8 < ln:
                sys.stdout.write(s_)
                sys.stdout.write('\n')
            else:
                s_ = s_ + '0' * (8 - len(s_))
                sys.stdout.write(s_)
                sys.stdout.write('\n')
