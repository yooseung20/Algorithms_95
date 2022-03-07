def longestPalindrome(s:str) -> str:
    # 팰린드롬을 판별하고 투 포인터 확장
    def expand(left:int, right:int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    # 해당 사항이 없을 때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s
    
    # 결과를 담을 문자열
    result =''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s)-1):
        result = max(result,
                    expand(i, i+1), # 팰린드롬이 짝수일 때
                    expand(i, i+2), # 팰린드롬이 홀수일 때
                    key=len)
    
    return result


# print(longestPalindrome("cbbd"))
# print(longestPalindrome("babad"))