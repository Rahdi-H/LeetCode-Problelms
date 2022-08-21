#-----Solution starts here
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return (strs[0])
        fw = strs[0]
        lfw = len(fw)
        for s in strs[1:]:
            while fw != s[0:lfw]:
                fw = fw[0:lfw - 1]
                lfw -= 1
                
                if lfw == 0:
                    return ""
        return fw
#-----Solution ends here