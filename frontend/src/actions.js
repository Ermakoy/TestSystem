import { makeAjaxRequest } from "./ajax";

export const REQUEST_SUBJECTS = 'REQUEST_SUBJECTS';
function requestSubjects() {
	return {
		type: REQUEST_SUBJECTS
	};
}

export const RECEIVE_SUBJECTS = 'RECEIVE_SUBJECTS';
function receiveSubjects(json) {
	return {
		type: RECEIVE_SUBJECTS,
		subjects: JSON.parse(json)
	};
}

export const SUBJECT_WAS_SELECTED = 'SUBJECT_WAS_SELECTED';
export function subjectSelected(subjectQueryName, subjectName) {
	return {
		type: SUBJECT_WAS_SELECTED,
		subjectQueryName,
		subjectName
	}
}

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
		tests: JSON.parse(json)
	}
}

export const STATIC_TEST_WAS_SELECTED = 'STATIC_TEST_WAS_SELECTED';
function staticTestSelected(testId, subject) {
	return {
		type: STATIC_TEST_WAS_SELECTED,
		testId,
		subject
	};
}

export function fetchSubjects() {
	return function(dispatch) {
		dispatch(requestSubjects());
		return makeAjaxRequest(`api/v0/`)
			.then(json => dispatch(receiveSubjects(json)),
				error => console.log(error)
			);
	}
}

export function fetchStaticTests(subject) {
	return function(dispatch) {
		dispatch(requestStaticTests());
		return makeAjaxRequest(`api/v0/getinfostest?subject=${subject}`)
			.then(json => dispatch(receiveStaticTests(subject, json)),
				error => console.log(error)
			);
	}
}