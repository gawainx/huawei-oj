import sys
from collections import defaultdict


def check_brother(src, tar):
    if src == tar:
        return False
    chr2dict = defaultdict(int)
    for c in src:
        chr2dict[c] += 1

    for c in tar:
        if chr2dict[c] > 0:
            chr2dict[c] -= 1
        else:
            return False
    for k_, v in chr2dict.items():
        if v != 0:
            return False
    return True


if __name__ == '__main__':
    srcs = sys.stdin.readline().strip().split()
    target = srcs[-2]
    k = int(srcs[-1])
    brothers = []
    for word in srcs[1: -2]:
        if len(word) != len(target):
            continue
        else:
            if check_brother(word, target):
                if word not in brothers:
                    brothers.append(word)
    brothers.sort()
    print(len(brothers))
    if len(brothers) >= k:
        print(brothers[k - 1])
