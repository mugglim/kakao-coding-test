def solution(s):
    # call by value
    word_regex_dic = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for word_regex, repl in word_regex_dic.items():
        s = s.replace(word_regex, repl)

    return int(s)
