class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        :s = babad
        """
        map = []
        for i in range(0, len(s)+1):
            if self.isPalindrome(s[:i]):
                 map.append(s[:i])
        
        l = 0
        res = ""
        for i in range(0, len(map)):
            if len(map[i]) > l: res = map[i]
            l = len(map[i])
        print(res)

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        :s = babad
        """
        if len(s) < 2: return False
        return s == self.reverse(s)

    def reverse(self, s):
        res = ""
        for i in range(0, len(s)):
            res += s[len(s)-i-1]
        return res



print(Solution().isPalindrome("asa"))
Solution().longestPalindrome("asdsaaaaaaaaaaa")