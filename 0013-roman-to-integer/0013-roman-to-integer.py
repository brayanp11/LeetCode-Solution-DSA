class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        prev = 0
        res = 0
        for c in s:
            if roman_num[c] > prev:
                res += roman_num[c] - prev*2
                prev = roman_num[c]
            else:
                res += roman_num[c]
                prev = roman_num[c]

        return res


        