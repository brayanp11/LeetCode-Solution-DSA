class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binary = []
        for i in range(n + 1):
            binary.append(bin(i)[2:])

        return int("".join(binary), 2) % (10**9 + 7)