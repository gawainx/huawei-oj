import sys


def main():
    line = sys.stdin.readline()
    line = line.rstrip()
    print(len(line.split(' ')[-1]))


if __name__ == '__main__':
    main()
