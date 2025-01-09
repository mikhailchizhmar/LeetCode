# https://leetcode.com/problems/string-compression

def string_compression(chars: list[str]) -> int:
    max_len = 1
    chars.append("!!!")
    for i in range(1, len(chars)):
        if chars[i] == chars[i - 1]:
            max_len += 1
        else:
            number = str(max_len) if max_len > 1 else ''
            chars[0] += chars[i - 1] + number
            max_len = 1

    chars[0] = chars[0][1:]
    while len(chars) > 1:
        chars.pop()
    chars = list(chars[0])
    return len(chars)


assert string_compression(["a", "a", "b", "b", "c", "c", "c"]) == 6
assert string_compression(["a"]) == 1
assert string_compression(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) == 4
