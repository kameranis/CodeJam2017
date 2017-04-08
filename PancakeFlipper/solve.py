#!/usr/bin/env python

def solve():
    s, K = raw_input().split()
    K = int(K)
    s = [1 if c == '+' else 0 for c in s]
    l = len(s)
    count = 0
    for i in xrange(len(s) - K + 1):
        if(s[i] == 0):
            count += 1
            for j in xrange(i, i+K):
                s[j] = 1-s[j]
    if any(c == 0 for c in s):
        return "IMPOSSIBLE"
    return count

def main():
    T = int(raw_input())
    for t in xrange(T):
        print "Case #{}: {}".format(t+1, solve())


if __name__ == '__main__':
    main()
