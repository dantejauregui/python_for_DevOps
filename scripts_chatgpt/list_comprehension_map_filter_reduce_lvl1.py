# STAGE 1 — BASIC TRANSFORMATIONS ("map" thinking)
# Challenge 1: Double Values
# Input: [1,2,3]
# Output: [2,4,6]
# Constraint:
# Use map OR list comprehension

#ANSWER:
# def double(input):
#     return [x * 2 for x in input]
# print(double([1,2,3]))

#=========================================================

# Challenge 2: String Lengths
# Input: ["hi", "hello"]
# Output: [2,5]

#ANSWER:
# def strings(arrays):
#    return [len(x) for x in arrays]
# print(strings(["hi", "hello"]))

#=========================================================

# Challenge 3: Uppercase Words
# Input: ["a", "b", "c"]
# Output: ["A", "B", "C"]

#ANSWER:
# def upper(arrays):
#     return [x.upper() for x in arrays]
# print(upper(["a", "b", "c"]))

#=========================================================

# STAGE 2 — FILTER THINKING
# Challenge 4: Keep Even Numbers
# Input: [1,2,3,4]
# Output: [2,4]

#ANSWER:
# def filter_even(arr):
#     return [x for x in arr if x % 2 == 0]
# print(filter_even([1,2,3,4]))

#=========================================================

# Challenge 5: Remove Empty Strings
# Input: ["a", "", "b"]
# Output: ["a", "b"]

#ANSWER:
# def filter_empties(arr):
#     return [x for x in arr if x != ""]
#     #OR: return [x for x in arr if x ]
# print(filter_empties(["a", "", "b"]))

#=========================================================

# Challenge 6: Words Longer Than 3
# Input: ["hi","hello","yes"]
# Output: ["hello"]

#ANSWER:
def word_lengths(arr):
    return [x for x in arr if len(x) > 3]

# Debug using "uv run python scripts_chatgpt/list_comprehension_map_filter_reduce_lvl1.py":
print(word_lengths(["hi","hello","yes"]))

#=========================================================
