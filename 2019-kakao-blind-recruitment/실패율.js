function go(...args) {
	return args.reduce((x, f) => f(x));
}

function map(f, iter) {
	const res = [];

	for (const el of iter) {
		res.push(f(el));
	}
	return res;
}

function toFailure([stage, ...result]) {
	return [stage, result[0] / result[1]];
}

function counter(arr) {
	const counterMap = new Map();

	arr.forEach(el => {
		if (!counterMap.has(el)) counterMap.set(el, 0);
		counterMap.set(el, counterMap.get(el) + 1);
	});

	return Array.from(counterMap);
}

function solution(N, stages) {
	const gameResults = Array.from(Array(N + 1), (_, idx) => [idx, 0, 0]);
	const stageCounter = counter(stages);

	for (const [stage, count] of stageCounter) {
		for (let i = 1; i <= Math.min(stage, N); i++) {
			if (i === stage) {
				gameResults[stage][1] += count;
			}

			gameResults[i][2] += count;
		}
	}

	return go(
		gameResults.slice(1),
		gameResults => map(toFailure, gameResults),
		failureResults => failureResults.sort((a, b) => b[1] - a[1]),
		failureResults => map(failureResult => failureResult[0], failureResults),
	);
}
