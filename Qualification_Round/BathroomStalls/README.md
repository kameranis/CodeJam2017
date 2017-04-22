# Problem

A certain bathroom has N + 2 stalls in a single row; the stalls on the left and right ends are permanently occupied by the bathroom guards. The other N stalls are for users.

Whenever someone enters the bathroom, they try to choose a stall that is as far from other people as possible. To avoid confusion, they follow deterministic rules: For each empty stall S, they compute two values LS and RS, each of which is the number of empty stalls between S and the closest occupied stall to the left or right, respectively. Then they consider the set of stalls with the farthest closest neighbor, that is, those S for which min(LS, RS) is maximal. If there is only one such stall, they choose it; otherwise, they choose the one among those where max(LS, RS) is maximal. If there are still multiple tied stalls, they choose the leftmost stall among those.

K people are about to enter the bathroom; each one will choose their stall before the next arrives. Nobody will ever leave.

When the last person chooses their stall S, what will the values of max(LS, RS) and min(LS, RS) be?

Solving this problem

This problem has 2 Small datasets and 1 Large dataset. You must solve the first Small dataset before you can attempt the second Small dataset. You will be able to retry either of the Small datasets (with a time penalty). You will be able to make a single attempt at the Large, as usual, only after solving both Small datasets.

Input

The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with two integers N and K, as described above.

Output

For each test case, output one line containing Case #x: y z, where x is the test case number (starting from 1), y is max(LS, RS), and z is min(LS, RS) as calculated by the last person to enter the bathroom for their chosen stall S.

```
Input			Output
5
4 2				Case #1: 1 0
5 2				Case #2: 1 0
6 2				Case #3: 1 1
1000 1000		Case #4: 0 0
1000 1			Case #5: 500 499
```

# Solution

First off there is just one space of size *N*. In each step the largest size of any space will break into two parts. `size/2` and `(size-1)/2`. The trick that will lead to a speedy solution is there is no reason to break the spaces one by one, but  spaces of the same sizes can be broken together. Starting off, each space occurs only once, but a few steps down the recursion there will be exponentially many occurences. Because each time smaller spaces are spawned, all there is to do is check the end of our `deque` and if it's the same space, just add to the record otherwise insert a new one. When all K people have been assigned, return `size/2` as max and `(size-1)/2` as min

The complexity of this solution is O(log*N*) at the worst, since the counts of the spaces are growing exponentially. Someone probably has a better reasoning than that.
