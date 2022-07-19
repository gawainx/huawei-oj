import sys

if __name__ == '__main__':
    src = sys.stdin.readline()
    src = src.strip()
    lt = list(src)
    print("".join(reversed(lt)))