import re
from itertools import permutations


def calc(x, y, opt):
    # for not using eval function
    if opt == "*":
        return x * y
    if opt == "+":
        return x + y
    if opt == "-":
        return x - y


def calc_by_optorder(splited_expression, opt_order):
    # immutable
    _splited_expression = [*splited_expression]

    for opt in opt_order:
        stack = []
        for el in _splited_expression:
            if not stack or type(el) != int:
                stack.append(el)
            else:
                if stack[-1] == opt:
                    _opt = stack.pop()
                    x = stack.pop()
                    stack.append(calc(x, el, _opt))
                else:
                    stack.append(el)

        _splited_expression = [*stack]

    return abs(_splited_expression[0])


def solution(expression):
    expression_num_list = list(map(int, re.split("[*+-]", expression)))
    expression_opt_list = re.findall("[*+-]", expression)
    opt_set = set(expression_opt_list)
    splited_expression = []

    ans = 0
    n = len(expression_num_list)

    for i in range(n):
        if i != n-1:
            splited_expression.append(expression_num_list[i])
            splited_expression.append(expression_opt_list[i])
        else:
            splited_expression.append(expression_num_list[i])

    for opt_order in permutations(opt_set):
        ans = max(ans, calc_by_optorder(splited_expression, opt_order))

    return ans
