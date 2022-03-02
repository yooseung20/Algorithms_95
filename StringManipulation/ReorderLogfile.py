def reorderLogfile(logfile:list):
    letter = []
    digit = []

    for log in logfile:
        # str.split() -> index 1 번 : 숫자인지 확인 
        if log.split()[1].isdigit():
            digit.append(log)
        else:
            letter.append(log)
    
    # sort : 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
    # 숫자 log는 입력 순서대로 한다.
    
    letter.sort(key = lambda x : (x.split()[1:],x.split()[0]))

    # 문자로 구성된 로그가 숫자 로그보다 먼저 온다.
    return letter + digit


logfile = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']

print(reorderLogfile(logfile))