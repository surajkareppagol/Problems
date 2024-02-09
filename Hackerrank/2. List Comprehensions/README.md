# 2. List Comprehensions

Let's learn about list comprehensions! You are given three integers x, y, z and representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k is not equal to n.

Please use list comprehensions rather than multiple loops, as a learning exercise.

```txt
Example

x = 1
y = 1
z = 2
n = 3

Print an array of the elements that do not sum to n = 3.

[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]
```

```txt
Input Format

Four integers x, y, z and n, each on a separate line.
```

```txt
Constraints

Print the list in lexicographic increasing order.
```

```txt
Sample Input 0

1
1
1
2
```

```txt
Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```

```txt
Explanation 0

Remove all arrays that sum to n = 2 to leave only the valid permutations.
```

```txt
Sample Input 1

2
2
2
2
```

```txt
Sample Output 1

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
```
