import thunkMiddleware from 'redux-thunk';
import { createStore, applyMiddleware } from 'redux';
import { fetchStaticTests } from './actions';
import reducer from './reducer';

console.log("Hello! I was included!");


// const store = createStore(
// 	reducer,
// 	applyMiddleware(
// 		thunkMiddleware
// 	)
// );

//store.dispatch(fetchStaticTests('math'));