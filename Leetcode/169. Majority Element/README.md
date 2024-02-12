# 169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

```txt
Example 1:

Input: nums = [3,2,3]
Output: 3
```

```txt
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

```txt
Constraints:

n == nums.length
1 <= n <= 5 * 10 ^ 4
-10 ^ 9 <= nums[i] <= 10 ^ 9
```

## Quick Note

So, i first had implemented it using dictionaries, and it took around 145ms, and then i came across `Boyer-Moore Majority Voting Algorithm` and used the code provided [here](https://www.geeksforgeeks.org/boyer-moore-majority-voting-algorithm/), and it took around 125ms, yes better than first approach, and it was awesome.
