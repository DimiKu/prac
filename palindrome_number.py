first = 121
second = -121
third = 10


class Solution:
    def isPalindrome(self, x: int) -> bool:
        pal_list = []
        for i in str(x):
            pal_list.append(i)

        return pal_list == pal_list[::-1]

sol = Solution()

print(sol.isPalindrome(first))
print(sol.isPalindrome(second))
print(sol.isPalindrome(third))
