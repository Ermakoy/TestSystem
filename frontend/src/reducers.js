import { combineReducers } from "redux";
import {
	REQUEST_SUBJECTS,
	RECEIVE_SUBJECTS,
	SUBJECT_WAS_SELECTED,
	REQUEST_STATIC_TESTS,
	RECEIVE_STATIC_TESTS
} from "./actions";

function subjectsList(state = {
	isFetching: false,
	subjects: []
}, action) {
	switch (action.type) {
		case REQUEST_SUBJECTS:
			return {
				...state,
				isFetching: true
			}
		case RECEIVE_SUBJECTS:
			return {
				...state,
				isFetching: false,
				subjects: action.subjects
			}
		default:
			return state;		
	}
}

function selectedSubject(state = {
	isSelected: false,
	queryName: null,
	name: null
}, action) {
	if (action.type === SUBJECT_WAS_SELECTED) {
		return {
			isSelected: true,
			queryName: action.subjectQueryName,
			name: action.subjectName
		};
	} else {
		return state;
	}
}

function staticTests(state = {
	isFetching: false,
	tests: []
}, action) {
	switch (action.type) {
		case REQUEST_STATIC_TESTS:
			return {
				...state,
				isFetching: true
			}
		case RECEIVE_STATIC_TESTS:
			return {
				...state,
				isFetching: false,
				tests: action.tests
			}
		default:
			return state;		
	}
}

export default combineReducers({
	subjectsList,
	selectedSubject,
	staticTests
});