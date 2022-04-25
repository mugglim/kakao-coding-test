class Trie {
	#head = new Map();

	constructor() {}

	insert(word) {
		let curr = this.#head;

		for (const ch of word) {
			if (!curr.has(ch)) curr.set(ch, new Map());
			curr = curr.get(ch);

			if (!curr.has('child')) curr.set('child', 0);
			curr.set('child', curr.get('child') + 1);
		}
	}

	query(word) {
		let cnt = 0;
		let curr = this.#head;

		for (const ch of word) {
			curr = curr.get(ch);
			cnt += 1;

			if (curr.get('child') === 1) break;
		}

		return cnt;
	}
}

function solution(words) {
	const trie = new Trie();

	words.forEach(word => trie.insert(word));

	return words.map(word => trie.query(word)).reduce((a, b) => a + b, 0);
}

solution(['go', 'gone', 'guild']);
