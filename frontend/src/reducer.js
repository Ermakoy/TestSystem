import { combineReducers } from "redux";
import {
	REQUEST_STATIC_TESTS,
	RECEIVE_STATIC_TESTS
} from "./actions";

export default function(state={}, action) {
	console.log(action);
	return state;
}