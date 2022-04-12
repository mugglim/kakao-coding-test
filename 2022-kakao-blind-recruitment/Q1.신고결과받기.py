def solution(id_list, report, k):
    report_set = set(report)
    report_adj_dic = {id: [] for id in id_list}
    report_count_dic = {id: 0 for id in id_list}
    ans = []

    def is_mailed(id):
        return report_count_dic[id] >= k

    # 신고 결과 반영
    for report_id in report_set:
        from_id, to_id = report_id.split(" ")
        report_adj_dic[from_id].append(to_id)
        report_count_dic[to_id] += 1

    # 누적 신고 횟수를 통해 결과 반영
    for reported_id_list in report_adj_dic.values():
        mail_count = sum([1 for id in reported_id_list if is_mailed(id)])
        ans.append(mail_count)

    return ans
