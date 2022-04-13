KEYPAD_POINT_DIC = {
    '1': (0, 0), '2': (0, 1), '3': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '7': (2, 0), '8': (2, 1), '9': (2, 2),
    '*': (3, 0), '0': (3, 1), '#': (3, 2)
}

L_KEYPAD_LIST = [1, 4, 7]
R_KEYPAD_LIST = [3, 6, 9]


def dist_of(keypad1, keypad2):
    x1, y1 = KEYPAD_POINT_DIC[str(keypad1)]
    x2, y2 = KEYPAD_POINT_DIC[str(keypad2)]
    return abs(x1-x2) + abs(y1-y2)


def solution(numbers, hand):
    keypad = ['*', '#']
    ans = []

    for number in numbers:
        if number in L_KEYPAD_LIST:
            ans.append("L")
            keypad[0] = number
        elif number in R_KEYPAD_LIST:
            ans.append("R")
            keypad[1] = number
        else:
            l_dist = dist_of(keypad[0], number)
            r_dist = dist_of(keypad[1], number)

            if l_dist < r_dist:
                ans.append("L")
                keypad[0] = number
            elif l_dist > r_dist:
                ans.append("R")
                keypad[1] = number
            else:
                if hand == "left":
                    ans.append("L")
                    keypad[0] = number
                else:
                    ans.append("R")
                    keypad[1] = number

    return ''.join(ans)
