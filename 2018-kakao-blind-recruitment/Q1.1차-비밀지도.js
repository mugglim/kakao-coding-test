function binOf(len, dec) {
	const bin = dec.toString(2);
	return bin.padStart(len, '0');
}

function formatOf(bin_text) {
	return Array.from(bin_text)
		.map(x => (x === '1' ? '#' : ' '))
		.join('');
}

function solution(n, arr1, arr2) {
	return arr1.map((v1, i) => {
		const v2 = arr2[i];
		const bin = binOf(n, v1 | v2);
		return formatOf(bin);
	});
}
