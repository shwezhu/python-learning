import re


def replace_case_insensitive(string, pattern, replacement):
    regex = re.compile(pattern, re.IGNORECASE)
    result = re.sub(regex, replacement, string)
    return result


def deframe_ppp(frame):
    frame = frame[2:-2]
    frame = replace_case_insensitive(frame, '7D5E', '7E')
    frame = replace_case_insensitive(frame, '7D5D', '7D')
    return frame


# Test
message = '7e417d5d427d5e5070467e'
original_message = deframe_ppp(message)
# Will print the original sequence: 417D427E507046
print(original_message)
