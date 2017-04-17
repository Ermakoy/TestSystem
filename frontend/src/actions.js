import { makeAjaxRequest } from "./ajax";

export const REQUEST_STATIC_TESTS = 'REQUEST_STATIC_TESTS';
function requestStaticTests(subject) {
	return {
		type: REQUEST_STATIC_TESTS,
		subject
	};
}

export const RECEIVE_STATIC_TESTS = 'RECEIVE_STATIC_TESTS';
function receiveStaticTests(subject, json) {
	return {
		type: RECEIVE_STATIC_TESTS,
		subject,
		staticTests: JSON.parse(json)
	}
}

export function fetchStaticTests(subject) {
	return function(dispatch) {
		dispatch(requestStaticTests());
		return makeAjaxRequest(`api_url_here`)
			.then(json =>
				dispatch(receiveStaticTests(json))
			)
	}
}