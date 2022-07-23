import sys

if __name__ == '__main__':
    s1, s2 = sys.stdin.readline().strip().split()
    s = s1 + s2
    str_even = [(c, idx) for idx, c in enumerate(s) if idx % 2 == 0]
    str_odd = [(c, idx) for idx, c in enumerate(s) if idx % 2 == 1]
    str_even.sort(key=lambda x: x[0])
    str_odd.sort(key=lambda x: x[0])
    lt = ['' for _ in s]

    for idx, (c, _) in enumerate(str_even):
        lt[idx << 1] = c

    for idx, (c, _) in enumerate(str_odd):

        lt[(idx << 1) + 1] = c

    new_str = ''.join(lt)

    digit2hex = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
                 '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
                 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111',
                 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    bin2digits = {tuple(list(v)): k for k, v in digit2hex.items()}
    llt = []
    for c in lt:
        if c in digit2hex.keys():
            llt.append(bin2digits[tuple(list(reversed(list(digit2hex[c]))))].upper())
        else:
            llt.append(c)

    print(''.join(llt))
