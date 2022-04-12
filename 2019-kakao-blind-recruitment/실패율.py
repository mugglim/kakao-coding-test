from collections import Counter


def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


def to_failure(fail_user, challenge_user):
    return fail_user / challenge_user if challenge_user != 0 else 0


def solution(N, stages):
    game_result = [[i, 0, 0] for i in range(N + 1)]
    stage_counter = Counter(stages)

    for stage, count in stage_counter.items():
        for i in range(1, stage):
            game_result[i][2] += count

        if stage <= N:
            game_result[stage][1] += count
            game_result[stage][2] += count

    game_result = [[result[0], to_failure(*result[1:])]
                   for result in game_result[1:]]

    game_result.sort(key=lambda x: -x[1])

    return [result[0] for result in game_result]
