from itertools import combinations
from collections import Counter


def solution(orders, course):
    menu_dic = {pick : [] for pick in course}
    ans = []
    
    for order in orders:
        for pick in course:
            for item in combinations(order, pick):
                voted_menu = ''.join(sorted(item))
                menu_dic[pick].append(voted_menu)

    for voted_menu_list in menu_dic.values():
        voted_menu_couter = Counter(voted_menu_list)
        
        if voted_menu_couter:
            most_voted_count = voted_menu_couter.most_common(1)[0][1]
            ans.extend([k for [k,v] in voted_menu_couter.items() if v == most_voted_count and most_voted_count > 1 ])
    
    return sorted(ans)