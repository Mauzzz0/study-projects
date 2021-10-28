import re
def largest_substring(string):
    length = 0
    x = 0
    y = 0
    match = None
    for y in range(len(string)):
        for x in range(len(string)):
            substring = string[y:x]
            if len(list(re.finditer(re.escape(substring), string))) > 1 and len(substring) > length:
                match = substring
                length = len(substring)

    """finding parts of a string"""
    for j in range(1, len(match)):
        tmp_period = match[:j]
        if tmp_period * (len(match)//len(tmp_period)) == match:
            return tmp_period

print(largest_substring(str(1 / int(input()))))
