# Problem

You are about to host a fashion show to show off three new styles of clothing. The show will be held on a stage which is in the most fashionable of all shapes: an N-by-N grid of cells.

Each cell in the grid can be empty (which we represent with a . character) or can contain one fashion model. The models come in three types, depending on the clothing style they are wearing: +, x, and the super-trendy o. A cell with a + or x model in it adds 1 style point to the show. A cell with an o model in it adds 2 style points. Empty cells add no style points.

To achieve the maximum artistic effect, there are rules on how models can be placed relative to each other.

Whenever any two models share a row or column, at least one of the two must be a +.
Whenever any two models share a diagonal of the grid, at least one of the two must be an x.
Formally, a model located in row i0 and column j0 and a model located in row i1 and column j1 share a row if and only if i0 = i1, they share a column if and only if j0 = j1, and they share a diagonal if and only if i0 + j0 = i1 + j1 or i0 - j0 = i1 - j1.

For example, the following grid is not legal:
```
...
x+o
.+.
```
The middle row has a pair of models (x and o) that does not include a +. The diagonal starting at the + in the bottom row and running up to the o in the middle row has two models, and neither of them is an x.

However, the following grid is legal. No row, column, or diagonal violates the rules.

```
+.x
+x+
o..
```
Your artistic advisor has already placed M models in certain cells, following these rules. You are free to place any number (including zero) of additional models of whichever types you like. You may not remove existing models, but you may upgrade as many existing + and x models into o models as you wish, as long as the above rules are not violated.

Your task is to find a legal way of placing and/or upgrading models that earns the maximum possible number of style points.

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with one line with two integers N and M, as described above. Then, M more lines follow; the i-th of these lines has a +, x, or o character (the type of the model) and two integers Ri and Ci (the position of the model). The rows of the grid are numbered 1 through N, from top to bottom. The columns of the grid are numbered 1 through N, from left to right.

Output

For each test case, first output one line containing Case #x: y z, where x is the test case number (starting from 1), y is the number of style points earned in your arrangement, and z is the total number of models you have added and/or substituted in. Then, for each model that you have added or substituted in, output exactly one line in exactly the same format described in the Input section, where the character is the type of the model that you have added or substituted in. These z lines can be in any order.

If there are multiple valid answers, you may output any one of them.

Limits

1 ≤ T ≤ 100.</br>
1 ≤ N ≤ 100.</br>
1 ≤ Ci ≤ N, for all i.</br>
0 ≤ M ≤ N^2.</br>
No two pre-placed models appear in the same cell.
It is guaranteed that the set of pre-placed models follows the rules.
Small dataset

Ri = 1, for all i. (Any models that are pre-placed are in the top row. Note that you may add/replace models in that row and/or add models in other rows.)
Large dataset

1 ≤ Ri ≤ N, for all i.
Sample

```
Input		Output 
 
3			Case #1: 4 3
2 0			o 2 2
1 1			+ 2 1
o 1 1		x 1 1
3 4			Case #2: 2 0
+ 2 3		Case #3: 6 2
+ 2 1		o 2 3
x 3 1		x 1 2
+ 2 2
```

# Solution

I have solved only the small one in a constructive way. In total there can be 1 non `+` symbol in each row or column, so N in total. Also there can be 1 non `x` symbol in each diagonal and there exist 2N-2 points that lie in different diagonals. Of course there is intersection between the two but with a carefully placed `o` 3N-2 score can be achieved. I am sure that someone will be able to prove that this is so, but I didn't. A construction that can be done in an empty board follows:

First I place `o 1 1` then fill then entire first row with `+`. Then place `x i i` for i=2..N and fill in `+ N i` where i ranges from 2 to N-1. This gives a board like this

```
o + + + +
. x . . .
. . x . .
. . . x .
. + + + x
```
This is valid and provides the maximum 3\*5-2=13 points.
 
Now suppose there is an `x` somewhere in the first line which would make this illegal. Easy enough, move all the `x`s before it one column to the left and upgrade the top `x` to a `o`. If for example there was a point `x 1 3` this board would be produced.
```
+ + o + +
x . . . .
. x . . .
. . . x .
. + + + x
```
Remember that the initial state that is given is valid and therefore there can be only one non `+` in the first row. Because I utilise that heavily, this solution will not be valid against the large input. In fact, as portrayed in the second example, the maximum score can diminish if the initial models are placed badly.

Lastly there is one corner case that the construction must bear in mind, the `x 1 N` case, where the solution will end up with one point less, as it won't be able to put anything in the lower right. This is easily rectified.
```
+ + + + o
. . . x .
. . x . .
. x . . .
x + + + .
```
Instead the lower left is utilised.

The complexity of this solution is O(*N*). Basically there are four loops. One to read the points (which will be at most *N* since they all lie in the first row). One to fill the first row. One to fill the diagonal with `x` and one to fill the last line. This means that the small input can be solved up to very large numbers of *N*. I will suppose that this is not true in the case of independently placing models wherever the aides saw fit.
