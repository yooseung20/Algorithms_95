# // 풀이 3 -> 슬라이싱 이용하기

import re

def isPalindrome(s:str)-> bool:
    # 정규식으로 숫자, 문자를 제외한 불필요한 문자 삭제
    s = re.sub('[^a-z0-9]','',s)

    # 슬라이싱
    if s != s[::-1]:
        return False
    return True

def main():  
    print("문자를 입력하세요 : " )
    s = input()
    return isPalindrome(s) 

    
if __name__ == "__main__":
    print(main())