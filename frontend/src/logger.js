const logger = store => next => action => {
	if (action.type !== undefined) {
		console.log('dispatching: ', action.type);
	}
	let result = next(action);
	return result;
}

export default logger;