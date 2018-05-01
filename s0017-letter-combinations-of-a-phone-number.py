from itertools import product

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        s = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        return [''.join(x) for x in product(*[list(y) for x in list(digits) for y in [s[int(x)]]])] if len(digits)>0 else []


print Solution().letterCombinations("234")
