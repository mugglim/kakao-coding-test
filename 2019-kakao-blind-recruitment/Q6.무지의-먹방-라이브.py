# ref : https://www.youtube.com/watch?v=zpz8SMzwiHM

def solution(food_times, k):
    heap = []

    food_times = [[i+1, food_time] for i, food_time in enumerate(food_times)]
    food_times.sort(key=lambda x: (x[1], x[0]))

    # height, idx
    w = len(food_times)
    h = 0
    ans = None

    for i, food_time in enumerate(food_times):
        diff = (food_time[1] - h) * w

        if k >= diff:
            k -= diff
            h = food_time[1]
        else:
            k %= w
            ans = sorted(food_times[i:], key=lambda x: x[0])[k][0]
            break

        w -= 1

    return -1 if not ans else ans
