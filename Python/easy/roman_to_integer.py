# https://leetcode.com/problems/roman-to-integer

def roman_to_int(s: str) -> int:
    roman = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500,
             "CM": 900, "M": 1000}

    result = 0
    for i in range(len(s)):
        if i > 0 and (((s[i] == "V" or s[i] == "X") and s[i - 1] == "I")
                      or ((s[i] == "L" or s[i] == "C") and s[i - 1] == "X")
                      or ((s[i] == "D" or s[i] == "M") and s[i - 1] == "C")):
            result -= 2 * roman[s[i - 1]]

        result += roman[s[i]]

    return result
