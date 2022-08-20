#Roman number to Integer
#-----Solution starts here
class Solution:
    def romanToInt(self, s: str) -> int:
        romanTable = {
           "I" : 1,
           "V" : 5,
           "X" : 10,
           "L" : 50,
           "C" : 100,
           "D" : 500,
           "M" : 1000 
        }
        intrslt = 0
        last = "I"
        for i in s[::-1]:
            if romanTable[i] < romanTable[last]:
                intrslt -= romanTable[i]
            else:
                intrslt += romanTable[i]
            last = i
        return intrslt
#-----Solution ends here

#check below
a = Solution()
i = a.romanToInt("XII")
print(i)