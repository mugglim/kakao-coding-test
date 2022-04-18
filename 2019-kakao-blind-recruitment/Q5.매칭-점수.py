import re
from collections import Counter


def solution(word, pages):
    dic = {}
    ans = [0, 0]

    word = word.lower()
    meta_content_findall_regex = re.compile(
        r'<meta property="og:url" content="(.*)"/>')
    anchor_findall_regex = re.compile(r'<a href=(.*?)</a>')
    word_findall_regex = re.compile("[a-zA-Z]+")

    for page in pages:
        page = page.lower()
        page_url = re.findall(meta_content_findall_regex, page)[0]
        word_count = re.findall(word_findall_regex, page).count(word)
        anchor_url_list = list(map(
            lambda url: url.split(">")[0][1:-1],
            re.findall(anchor_findall_regex, page)
        )
        )
        link_score = 0 if not anchor_url_list else word_count / \
            len(anchor_url_list)

        dic[page_url] = {
            'word_count': word_count,
            'anchor_url_list': anchor_url_list,
            'score': [word_count, link_score, word_count]
            # default score / link score / match score
        }

    # 링크 점수 반영
    for page_url in dic.keys():
        for anchor_url in dic[page_url]['anchor_url_list']:
            if anchor_url in dic:
                dic[anchor_url]['score'][2] += dic[page_url]['score'][1]

    for i, v in enumerate(dic.values()):
        match_score = v['score'][2]

        if match_score > ans[1]:
            ans = [i, match_score]

    return ans[0]
