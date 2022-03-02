import re 
import collections

# collections.defaultdict 이용
def most_common_word(sentence:str, banned: list):
    # banned 단어를 제외하고 소문자로 된 list 만들기
    sentence = re.sub(r"[^a-zA-Z\s]",'', sentence).split()
    words = [word.lower() for word in sentence if word not in banned]
    
    # 단어 빈도수를 기록하는 dict 선언
    common = collections.defaultdict(int)
    for word in words:
        common[word] += 1
    
    # dict의 value값 기준으로 max값을 가지는 key값 출력
    return max(common, key=common.get)



paragraph = "Bob hit a ball, the hit BALL few far after it was hit."
banned = ["hit"]

print(most_common_word(paragraph, banned))