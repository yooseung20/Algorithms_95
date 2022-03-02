import re 
import collections

# most_common() 이용
def most_common_word(sentence:str, banned: list) -> list:
    sentence = re.sub(r"[^a-zA-Z\s]",'', sentence).split()
    words = [word.lower() for word in sentence if word not in banned]

    # collections.Counter(a).most_common(n)   : a의 요소를 세어, 최빈값 n개를 반환
    # 최빈값을 가지는 index 리턴
    return collections.Counter(words).most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL few far after it was hit."
banned = ["hit"]

print(most_common_word(paragraph, banned))