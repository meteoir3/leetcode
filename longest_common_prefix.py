class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :strs = ["flower","flow","flight"]
        :rtype: str
        """
        idx = 0
        res = ""
        if len(strs) == 0: return ""
        for ch in strs[0]:
            if self.is_prefix(strs, idx): res += ch
            idx += 1
        return res

    def is_prefix(self, strs, index):
        ch = strs[0][index]
        for str in strs:
            if len(str) < index+1: return False
            if str[index] != ch: return False
        return True
                


print(Solution().longestCommonPrefix(["flower","flow","flight"]))