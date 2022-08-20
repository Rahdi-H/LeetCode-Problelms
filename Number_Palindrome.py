class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reversed_number = 0
        digit = 0
        while x // (10**digit) != 0:
            reversed_number = (reversed_number * 10) + (x // (10**digit) % 10)
            digit += 1

        return(x == reversed_number)

#Checking below
a = Solution()
i = a.isPalindrome(121)
print(i)