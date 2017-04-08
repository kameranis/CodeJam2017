# Problem

Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest, her pencils are sorted from shortest to longest and her computers from oldest to newest. One day, when practicing her counting skills, she noticed that some integers, when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order. Some examples of this are 8, 123, 555, and 224488. She decided to call these numbers tidy. Numbers that do not have this property, like 20, 321, 495 and 999990, are not tidy.

She just finished counting all positive integers in ascending order from 1 to N. What was the last tidy number she counted?

Input

The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with a single integer N, the last number counted by Tatiana.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the last tidy number counted by Tatiana.

Input | Output
------|-------
4 |
132 | Case #1: 129
1000 | Case #2: 999
7 | Case #3: 7
111111111111111110 | Case #4: 99999999999999999

# Solution

Starting from left to right, if the current digit is larger than the previous one, then commit all the previous numbers to your solution. If it is the same as the previous one, then add it to a temporary solution. If it is smaller than the previous one, then first commit to your solution the digit you have in the temporary solution minus one and the rest of the digits are '9'. Special care should be taken in cases like #4, where the initial 1 becomes 0 and needs to be eliminated.
}

Other people have submitted solutions starting reversely from the end. Both solutions work well.

The complexity of this solution is O(logN), since we greedily decide for each digit without checking any other.
