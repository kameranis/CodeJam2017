#!/usr/bin/env python

def solve():
    D, N = [int(i) for i in raw_input().split()]
    riders = [[int(j) for j in raw_input().split()] for _ in xrange(N)]
    times = []
    for start, speed in riders:
        times.append((D-start)/float(speed))
    time = max(times)
    if time > 0:
        return float(D)/time
    else:
        return 0


def main():
    T = int(raw_input())
    for i in xrange(T):
        sol = solve()
        print 'Case #{}: {}'.format(i+1, sol)


if __name__ == '__main__':
    main()
