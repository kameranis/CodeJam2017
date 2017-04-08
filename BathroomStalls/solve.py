#!/usr/bin/env python

from collections import deque

def solve():
    N, K = [int(i) for i in raw_input().split()]
    records = deque([[N, 1]])
    while True:
        size, count = records[0]
        if count >= K:
            return size/2, (size-1)/2
        elif size == 0:
            return 0, 0
        else:
            K -= count
            if records[-1][0] == size/2:
                records[-1][1] += count
            else:
                records.append([size/2, count])
            if records[-1][0] == (size-1)/2:
                records[-1][1] += count
            else:
                records.append([(size-1)/2, count])
        records.popleft()

def main():
    T = int(raw_input())
    for t in xrange(T):
        print "Case #{}: {} {}".format(t+1, *solve())


if __name__ == '__main__':
    main()
