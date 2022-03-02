

# // 풀이 1 -> list로 풀기
def str_list(s):
    strs = []
    for char in s:
        # isalnum() 영문자, 숫자 여부를 판별하는 함수
        if char.isalnum():
            # 소문자로 변경해서 리스트에 넣기
            strs.append(char.lower())
    return strs


def isPalindrome(s:str) -> bool:
    strs = str_list(s)
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
        # 첫번째 문자와 마지막 문자 같은지 확인
            return False
    return True



def main():  
    print("문자를 입력하세요 : " )
    s = input()
    return isPalindrome(s) 

    
if __name__ == "__main__":
    print(main())