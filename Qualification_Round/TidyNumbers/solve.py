#!/usr/bin/env python

def solve():
    solution = []
    temp_sol = []
    s = raw_input()
    last = '0'
    for i, c in enumerate(s):
        if c > last:
            last = c
            solution.extend(temp_sol)
            temp_sol = [last]
        elif c == last:
            temp_sol.append(last)
        else:
            solution.append(chr(ord(last[0])-1))
            solution.extend(['9']*(len(temp_sol) + len(s) - i - 1))
            temp_sol = []
            break
    solution.extend(temp_sol)
    return ''.join(solution)


def main():
    T = int(raw_input())
    for t in xrange(T):
        print "Case #{}: {}".format(t+1, int(solve()))


if __name__ == '__main__':
    main()
