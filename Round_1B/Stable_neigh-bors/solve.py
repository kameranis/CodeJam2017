#!/usr/bin/env python

import time

def solve():
    orange, green, violet = False, False, False
    N, R, O, Y, G, B, V = [int(i) for i in raw_input().split()]
    if O > 0:
        B -= O
        orange = True
    if G > 0:
        R -= G
        green = True
    if V > 0:
        Y -= V
        yellow = True
    if (R > B + Y) or (B > Y + R) or (Y > R + B) or \
        ((Y == 0) and violet and ((B > 0) or (R > 0))) or \
        ((R == 0) and green and ((Y > 0) or (B > 0))) or \
        ((B == 0) and orange and ((R > 0) or (Y > 0))):
        return 'IMPOSSIBLE'
    colors = [[R, 0, 'R'], [B, 0, 'B'], [Y, 0, 'Y']]
    sol = []
    current = None
    while [c[0] for c in colors] != [0, 0, 0]:
        colors.sort(reverse=True)
        if colors[0][2] == current:
            current = colors[1][2]
            sol.append(current)
            colors[1][0] -= 1
            colors[0][1] -= 1
            colors[1][1] = 0
            colors[2][1] -= 1
        else:
            current = colors[0][2]
            sol.append(current)
            colors[0][0] -= 1
            colors[0][1] = 0
            colors[1][1] -= 1
            colors[2][1] -= 1
    for color, bastard, count in [('B', 'O', O), ('R', 'G', G), ('Y', 'V', V)]:
        if color not in sol:
            sol.extend(''.join([color+bastard]*count))
        else:
            pos = sol.index(color)
            sol.insert(pos, ''.join([color+bastard]*count))
    if sol[-1] == sol[0]:
        sol[-3], sol[-1] = sol[-1], sol[-3]
    return ''.join(sol)



def main():
    T = int(raw_input())
    for i in xrange(T):
        sol = solve()
        print 'Case #{}: {}'.format(i+1, sol)


if __name__ == '__main__':
    main()
