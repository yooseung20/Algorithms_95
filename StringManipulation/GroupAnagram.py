import collections
def groupAnagram(word_list:list) -> list:
    # 빈 list를 value로 갖는 dict 생성 
    group_dict = collections.defaultdict(list)

    # 동일한 char을 가진 경우끼리 모으기
    for word in word_list:
        group_dict[''.join(sorted(word))].append(word)
    
    # dict.values -> sort
    for k,v in group_dict.items():
        group_dict[k].sort(key = lambda x :[x[0], x[1]])
    

    return list(group_dict.values())
        

word_list =['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

print(groupAnagram(word_list))