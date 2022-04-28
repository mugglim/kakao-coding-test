function solution(new_id) {
	let ans = new_id
		.toLowerCase()
		.replace(/[^a-z\d\_\.\-]/g, '')
		.replace(/\.{2,}/g, '.')
		.replace(/^\.|\.$/, '')
		.replace(/^$/, 'a')
		.slice(0, 15)
		.replace(/\.$/, '');

	const { length } = ans;

	return length <= 2
		? ans.concat(ans.charAt(length - 1).repeat(3 - length))
		: ans;
}
