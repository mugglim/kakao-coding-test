import re

def solution(files):
    ans = []
    
    for file in files:
        head = re.search('[^\d]+', file)[0]
        file = file[len(head):]
        num = re.search('\d{1,5}', file)[0]
        tail = file[len(num):]
        ans.append([head, num, tail])
    
    ans.sort(key=lambda x:(x[0].lower(), int(x[1])))
    return list(map(lambda x: ''.join(x), ans))