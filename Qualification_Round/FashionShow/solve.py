#!/usr/bin/env python

def solve():
    N, M = [int(i) for i in raw_input().split()]
    table = [['.']*N for _ in xrange(N)]
    bad_j = None
    points = []
    # Read standard points
    for _ in xrange(M):
        c, i, j = raw_input().split()
        i, j = int(i)-1, int(j)-1
        # I don't want any 'x' on the first row
        if c == 'x':
            bad_j = j
            c = 'o'
            points.append(('o', i+1, j+1))
        table[i][j] = c
        if c == 'o':
            bad_j = j
    # If there were all '+' on the first row, then add '0' at (0, 0)
    if bad_j is None:
        table[0][0] = 'o'
        bad_j = 0
        points.append(('o', 1, 1))
    # Add '+' in the rest of the first row
    for j in xrange(N):
        if j != bad_j and table[0][j] != '+':
            table[0][j] = '+'
            points.append(('+', 1, j+1))
    j = 0
    if bad_j != N-1:
        for i in xrange(1, N):
            if j == bad_j:
                j += 1
            table[i][j] = 'x'
            points.append(('x', i+1, j+1))
            j += 1
    else:
        for i in xrange(1, N):
            if N-1-j == bad_j:
                j += 1
            points.append(('x', i+1, N-j))
            table[i][N-1-j] = 'x'
            j += 1

    for j in xrange(1, N-1):
        if table[-1][j] != 'x':
            table[-1][j] = '+'
            points.append(('+', N, j+1))
    s = 0
    for line in table:
        for elem in line:
            if elem in ['+', 'x']:
                s += 1
            elif elem == 'o':
                s += 2
    print s, len(points)
    for r in points:
        print "{} {} {}".format(*r)


def main():
    T = int(raw_input())
    for t in xrange(T):
        print "Case #{}:".format(t+1),
        solve()


if __name__ == '__main__':
    main()

# This is one of the worst codes I have written
