# 투포인터 이용
def reverseString(s: list) -> list:
    left, right = 0, len(s)-1

    while left < right :
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s

s = ['h','e','l','l','o']
print(reverseString(s))





