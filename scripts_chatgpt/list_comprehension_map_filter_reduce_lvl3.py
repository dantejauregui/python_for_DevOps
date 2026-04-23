# STAGE 4 — INTRO TO REDUCE (aggregation)
# You must import "Functools" which is part of Python’s standard library:
from functools import reduce


# Challenge 10: Sum List
# Input: [1,2,3,4]
# Output: 10
# **(no "sum()" allowed)

#ANSWER (giving an initial value "0" in Reduce function, because it handles empty lists safely):
# def adding(total_so_far, current_number):
#     return total_so_far + current_number

# def sum_list(arr):
#     return reduce(adding, arr, 0)

# print(f'Input: [1, 2, 3, 4] -> Output: {sum_list([1, 2, 3, 4])}')

#=========================================================


# Challenge 11: Multiply All Values
# Input: [1,2,3,4]
# Output: 24

#ANSWER:
# def accumulator(total_so_far, current_number):
#     return total_so_far * current_number

# def mult_list(arr):
#     return reduce(accumulator, arr, 1)

# print(f'Input: [1, 2, 3, 4] -> Output: {mult_list([1, 2, 3, 4])}')

#=========================================================


# Challenge 12: Longest String
# Input: ["hi","hello","hey"]
# Output: "hello"

#ANSWER:
# def helper(long_so_far, current_str):
#     if len(current_str) > len(long_so_far):
#         long_so_far = current_str
#     return long_so_far

# def detect_longest(arr):
#     return reduce(helper, arr, "")


# Debug using "uv run python scripts_chatgpt/list_comprehension_map_filter_reduce_lvl3.py":
# print(f'Input: ["hi","hello","hey"] -> Output: {detect_longest(["hi","hello","hey"])}')

#=========================================================


# STAGE 5 — REAL PROBLEMS

# Challenge 13: Sum of Squares of Even Numbers
# Input: [1,2,3,4]
# Output: 20

#ANSWER:
