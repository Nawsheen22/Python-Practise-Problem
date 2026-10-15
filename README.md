# Python Practice Problems

My Python practice: beginner exercises plus LeetCode solutions, each with a written explanation of the approach and its time/space complexity.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![LeetCode](https://img.shields.io/badge/LeetCode-22%20solved-orange?logo=leetcode&logoColor=white)

## Repository Structure

```
Python-Practise-Problem/
├── Problem00.py ... problem52.py   # Beginner Python exercises
└── leetcode/
    ├── easy/
    ├── medium/
    └── hard/
```

## LeetCode Progress

| Easy | Medium | Hard | Total |
|:----:|:------:|:----:|:-----:|
| 11   | 10     | 1    | **22** |

### Easy

| # | Problem | Topic | Solution |
|---|---------|-------|----------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Hash Table | [Python](leetcode/easy/0001_two_sum.py) |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Stack | [Python](leetcode/easy/0020_valid_parentheses.py) |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Linked List | [Python](leetcode/easy/0021_merge_two_sorted_lists.py) |
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Dynamic Programming | [Python](leetcode/easy/0070_climbing_stairs.py) |
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Tree, DFS | [Python](leetcode/easy/0104_maximum_depth_of_binary_tree.py) |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Array | [Python](leetcode/easy/0121_best_time_to_buy_and_sell_stock.py) |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Two Pointers | [Python](leetcode/easy/0125_valid_palindrome.py) |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Linked List | [Python](leetcode/easy/0206_reverse_linked_list.py) |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Hash Table | [Python](leetcode/easy/0217_contains_duplicate.py) |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Hash Table | [Python](leetcode/easy/0242_valid_anagram.py) |
| 704 | [Binary Search](https://leetcode.com/problems/binary-search/) | Binary Search | [Python](leetcode/easy/0704_binary_search.py) |

### Medium

| # | Problem | Topic | Solution |
|---|---------|-------|----------|
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Sliding Window | [Python](leetcode/medium/0003_longest_substring_without_repeating_characters.py) |
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Two Pointers | [Python](leetcode/medium/0011_container_with_most_water.py) |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | Two Pointers, Sorting | [Python](leetcode/medium/0015_3sum.py) |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Hash Table | [Python](leetcode/medium/0049_group_anagrams.py) |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Kadane's Algorithm | [Python](leetcode/medium/0053_maximum_subarray.py) |
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Sorting | [Python](leetcode/medium/0056_merge_intervals.py) |
| 146 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Design | [Python](leetcode/medium/0146_lru_cache.py) |
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | DFS, Matrix | [Python](leetcode/medium/0200_number_of_islands.py) |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Prefix Product | [Python](leetcode/medium/0238_product_of_array_except_self.py) |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) | Dynamic Programming | [Python](leetcode/medium/0322_coin_change.py) |

### Hard

| # | Problem | Topic | Solution |
|---|---------|-------|----------|
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Two Pointers | [Python](leetcode/hard/0042_trapping_rain_water.py) |

## Solution Format

Every LeetCode file follows the same layout:

1. **Header**: problem number, title, link, difficulty and topics
2. **Approach**: a plain-English explanation of the idea
3. **Complexity**: time and space
4. **Code**: a `Solution` class in LeetCode's format
5. **Tests**: example cases that run when the file is executed

## How to Run

```bash
python leetcode/easy/0001_two_sum.py
```

Each file prints `All tests passed` when its solution is correct.
