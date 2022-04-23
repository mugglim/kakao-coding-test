function matchOf(str, regex) {
	const res = str.match(regex);
	return res ? res[0] : null;
}

function solution(dartResult) {
	const scoreList = [];
	const bonusObj = { S: 1, D: 2, T: 3 };
	const optionObj = { '*': 2, '#': -1 };

	const handleOption = (score, option) => {
		if (option === '*' && scoreList.length) {
			scoreList[scoreList.length - 1] *= optionObj[option];
		}

		return score * optionObj[option];
	};

	const dartResultRegex = /\d{1,2}[SDT][*#]?/g;
	const scoreRegex = /\d{1,2}/;
	const bonusRegex = /[SDT]/;
	const optionRegex = /[*#]/;

	const resultList = dartResult.match(dartResultRegex);

	for (const result of resultList) {
		let score = +matchOf(result, scoreRegex);
		const bonus = matchOf(result, bonusRegex);
		const option = matchOf(result, optionRegex);

		score **= bonusObj[bonus];

		if (option) {
			score = handleOption(score, option);
		}
		scoreList.push(score);
	}

	return scoreList.reduce((a, b) => a + b);
}
