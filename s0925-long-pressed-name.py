class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        count = len(name)
        for c in typed:
            if i < count and name[i] == c:
                i += 1
                continue
            elif i > 0 and name[i - 1] == c:
                continue
            return False
        return i == count


print(Solution().isLongPressedName("pyplrz", "ppyypllr"))
