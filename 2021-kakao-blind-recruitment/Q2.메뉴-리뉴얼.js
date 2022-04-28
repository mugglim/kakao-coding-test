const cmp = (a, b) => a.localeCompare(b);

const sortString = text =>
	Array.from(text)
		.sort((a, b) => a.localeCompare(b))
		.join('');

class Counter {
	counter = new Map();

	constructor(arr) {
		arr.forEach(item => this.set(item));
	}

	get(key) {
		if (!this.counter.has(key)) new Error('key is not exist');
		return this.counter.get(key);
	}

	set(key) {
		if (!this.counter.has(key)) this.counter.set(key, 0);
		this.counter.set(key, this.counter.get(key) + 1);
	}

	mostCommon() {
		const maxCount = Math.max(...this.counter.values());
		return Array.from(this.counter.entries()).filter(
			([_, v]) => v === maxCount,
		);
	}
}

function combination(arr, pick) {
	let ans = [];

	const backtrack = (item, rest) => {
		if (item.length === pick) ans.push(item);
		Array.from(rest).forEach((v, i) => backtrack(item + v, rest.slice(i + 1)));
	};

	backtrack([], arr);
	return ans;
}

function solution(orders, course) {
	let ans = [];
	const menuMap = new Map(course.map(v => [v, new Array()]));
	const sortedOrders = orders.map(sortString);

	for (const order of sortedOrders) {
		for (const pick of course) {
			combination(order, pick).forEach(item => {
				menuMap.get(pick).push(item);
			});
		}
	}

	for (const items of menuMap.values()) {
		const counter = new Counter(items);
		const mostCommonItems = counter.mostCommon();

		if (!mostCommonItems.length || mostCommonItems[0][1] < 2) continue;
		mostCommonItems.forEach(item => ans.push(item[0]));
	}

	return ans.sort(cmp);
}
