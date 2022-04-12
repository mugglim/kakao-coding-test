import math


def minute_of(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m


def price_of(fees, use_minute_list):
    default_min, default_fee, unit_min, unit_fee = fees
    res = []

    for use_minute in use_minute_list:
        remain_minute = use_minute - default_min if use_minute > default_min else 0
        price = default_fee + (math.ceil(remain_minute / unit_min)) * unit_fee
        res.append(price)

    return res


def solution(fees, records):
    car_num_list = sorted(list(set(map(lambda x: x.split(' ')[1], records))))
    car_time_dic = {car_num: 0 for car_num in car_num_list}
    car_in_dic = {car_num: 0 for car_num in car_num_list}

    for record in records:
        t, car_num, opt = record.split(" ")

        if opt == "IN":
            # 입차 처리
            car_in_dic[car_num] = minute_of(t)
        else:
            # 출차 처리
            car_time_dic[car_num] += minute_of(t) - car_in_dic[car_num]
            del car_in_dic[car_num]

    # 입차는 했는데, 출차 하지 않는 차량들 처리
    for car_num, minute in car_in_dic.items():
        car_time_dic[car_num] += minute_of("23:59") - car_in_dic[car_num]
    car_in_dic = {}

    return price_of(fees, car_time_dic.values())
