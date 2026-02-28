class Solution:
    def reverseByType(self, s: str) -> str:
        s = list(s)
        
        def reverse_condition(arr, condition_fn):
            l, r = 0, len(arr) - 1

            while l < r:
                while l < r and not condition_fn(arr[l]):
                    l += 1
                while l < r and not condition_fn(arr[r]):
                    r -= 1
                if l < r:
                    arr[l], arr[r] = arr[r], arr[l]
                    l += 1
                    r -= 1

        reverse_condition(s, lambda char: char.isalpha())
        reverse_condition(s, lambda char: not char.isalpha())
        
        return "".join(s)