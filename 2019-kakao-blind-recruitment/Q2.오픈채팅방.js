function solution(record) {
	const nicknameMap = new Map();
	const queryList = [];

	const handleSetRecord = ([opt, uID, ...rest]) => {
		if (opt === 'Enter' || opt === 'Change') {
			nicknameMap.set(uID, rest[0]);
		}

		if (opt === 'Enter' || opt === 'Leave') {
			queryList.push([uID, opt]);
		}
	};

	const handleQuery = ([uID, opt]) => {
		const nickName = nicknameMap.get(uID);

		if (opt === 'Enter') {
			return `${nickName}님이 들어왔습니다.`;
		}

		return `${nickName}님이 나갔습니다.`;
	};

	record.map(el => el.split(' ')).forEach(handleSetRecord);
	return queryList.map(handleQuery);
}
