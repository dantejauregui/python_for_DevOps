# STAGE 3 — MAP + FILTER COMBO
# Challenge 7: Square Only Even Numbers
# Input: [1,2,3,4]
# Output: [4,16]

#ANSWER:
# def square_even(arr):
#     return [x**2 for x in arr if x%2 == 0]
# print(square_even([1,2,3,4]))

#=========================================================

# Challenge 8: Uppercase Words > 3 chars
# Input: ["hi","hello","world"]
# Output: ["HELLO","WORLD"]

#ANSWER:
# def uppercase_3chars(arr):
#     return [x.upper() for x in arr if len(x) > 3]
# print(uppercase_3chars(["hi","hello","world"]))

#=========================================================

# Challenge 9: Extract Digits from Strings
# Input: ["a1","b2","c3"]
# Output: [1,2,3]

#ANSWER:
def extractor(str):
    # For each character in the string, if it's a digit, convert it to an integer.
    return [int(char) for char in str if char.isdigit()]

def mapping_digits(arr):
    # This is a nested list comprehension. It performs the following:
    # 1. Start with "for text in arr", and for each 'text' in the input list 'arr'...
    # 2. It calls our 'extractor(text)' function, which returns a list (e.g., [4, 5]).
    # 3. It then loops through that returned list ("for char in ...")
    # 4. It adds each individual char to the final list.
    return [char for text in arr for char in extractor(text)]


# Debug using "uv run python scripts_chatgpt/list_comprehension_map_filter_reduce_lvl2.py":
print(f'Input: ["a1","b2","c3"] -> Output: {mapping_digits(["a1","b2","c3"])}')
print(f'Input: ["abc", "d45", "e", "f6g7"] -> Output: {mapping_digits(["abc", "d45", "e", "f6g7"])}')
