# // 풀이 2 -> deque 이용하기
import collections

def isPalindrome(s:str) -> bool:
    # 자료형 데크로 선언 -> append, pop 속도가 list에 비해 월등히 좋음
    strs = collections.deque()
    
    for char in s:
        if char.isalnum():
            strs.append(char)
    
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True
            


def main():  
    print("문자를 입력하세요 : " )
    s = input()
    return isPalindrome(s) 

    
if __name__ == "__main__":
    print(main())