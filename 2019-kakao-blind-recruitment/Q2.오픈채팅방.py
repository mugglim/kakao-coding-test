def solution(record):
    nickname_dic = {}
    query_list = []

    def get_enter_msg(nickname):
        return f"{nickname}님이 들어왔습니다."

    def get_out_msg(nickname):
        return f"{nickname}님이 나갔습니다."

    def handle_query(opt, u_id):
        nickname = nickname_dic[u_id]

        if opt == "Enter":
            return get_enter_msg(nickname)
        else:
            return get_out_msg(nickname)

    for r in record:
        opt, u_id, *rest = r.split(" ")

        if opt in ["Enter", "Change"]:
            nickname = rest[0]
            nickname_dic[u_id] = nickname

        if opt in ["Enter", "Leave"]:
            query_list.append([opt, u_id])

    return [handle_query(*query) for query in query_list]
