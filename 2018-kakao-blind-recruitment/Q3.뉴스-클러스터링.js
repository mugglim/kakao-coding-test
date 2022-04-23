function solution(str1, str2) {
	str1 = str1.toLowerCase();
	str2 = str2.toLowerCase();

	const counterOf = (s, n) => {
		const { length } = s;

		return Array.from(Array(length - n + 1), (_, i) => s.substr(i, n))
			.filter(word => !word.match(/[^a-zA-Z]/))
			.reduce((res, word) => {
				if (!res.hasOwnProperty(word)) res[word] = 0;
				res[word] += 1;
				return res;
			}, {});
	};

	const intersection = (counterA, counterB) => {
		return Object.keys(counterA)
			.filter(prop => counterB.hasOwnProperty(prop))
			.map(prop => Math.min(counterA[prop], counterB[prop]))
			.reduce((a, b) => a + b, 0);
	};

	const union = (counterA, counterB) => {
		const v1 = Object.keys(counterA)
			.map(prop => {
				return counterB.hasOwnProperty(prop)
					? Math.max(counterA[prop], counterB[prop])
					: counterA[prop];
			})
			.reduce((a, b) => a + b, 0);

		const v2 = Object.keys(counterB)
			.filter(prop => !counterA.hasOwnProperty(prop))
			.map(prop => counterB[prop])
			.reduce((a, b) => a + b, 0);

		return v1 + v2;
	};

	const counterA = counterOf(str1, 2);
	const counterB = counterOf(str2, 2);

	const inter = intersection(counterA, counterB);
	const uni = union(counterA, counterB);

	const similarity = uni > 0 ? inter / uni : 1;

	return Math.floor(65536 * similarity);
}
