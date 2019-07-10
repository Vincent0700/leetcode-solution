class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        arr = list(S)
        count = len(arr)
        j = count - 1
        for i in range(count):
            if i > j:
                break
            if arr[i].isalpha():
                while(not arr[j].isalpha()):
                    j -= 1
                c = arr[i]
                arr[i] = arr[j]
                arr[j] = c
                j -= 1
        return ''.join(arr)

print(Solution().reverseOnlyLetters("a-bC-dEf-ghIj"))