# write the function is_anagram
def is_anagram(test, original):
    low1 = test.lower()
    low2 = original.lower()
    
    if len(low1) != len(low2):
        return False
    else:
        if ''.join(sorted(low1)) != ''.join(sorted(low2)):
            return False
        else:
            return True

#debuging using "uv run python py_scripts_codewars.com/anagram.py":
print(is_anagram("jKNXOI", "XKnIOj"))


# challenge url: https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/python