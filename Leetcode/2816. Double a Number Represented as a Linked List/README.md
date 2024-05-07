# 2816. Double a Number Represented as a Linked List

You are given the `head` of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the `head` of the linked list after doubling it.

![Linked List](https://assets.leetcode.com/uploads/2023/05/28/example.png)

```txt
Example 1:

Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.
```

![Linked List](https://assets.leetcode.com/uploads/2023/05/28/example2.png)

```txt
Example 2:

Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list represents the number 999 * 2 = 1998.
```

```txt
Constraints:

- The number of nodes in the list is in the range [1, 104]
- 0 <= Node.val <= 9
- The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.
```
