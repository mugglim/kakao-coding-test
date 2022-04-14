import re


def solution(dartResult):
    bonus_dic = {'S': '1', 'D': '2', 'T': '3'}
    option_dic = {'*': '2', '#': '-1'}

    score_list = []

    regex = re.compile('\d{1,2}[SDT][*#]?')
    dart_result_list = re.findall(regex, dartResult)

    for dart_result in dart_result_list:
        score_search = re.search('\d{1,2}', dart_result)[0]
        bonus_search = re.search('[SDT]', dart_result)[0]
        option_search = re.search('[*#]', dart_result)

        result_score = int(score_search) ** int(bonus_dic[bonus_search])

        if option_search:
            option = option_search[0]
            option_num = int(option_dic[option])

            if option == '*' and score_list:
                score_list[-1] *= option_num
            result_score *= option_num

        score_list.append(result_score)

    return sum(score_list)
