class Solution:
    def compress(self, chars: List[str]) -> int:
        left, right = 0, 0

        while right < len(chars):
            curr_char = chars[right]
            count = 0

            while right < len(chars) and chars[right] == curr_char:
                right += 1
                count += 1

            chars[left] = curr_char
            left += 1

            if count > 1:
                for digit in str(count):
                    chars[left] = digit
                    left += 1
                count = 0

        return left