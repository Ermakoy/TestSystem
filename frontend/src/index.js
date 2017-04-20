import React from 'react';
import ReactDOM from 'react-dom';

import { Provider } from 'react-redux';
import thunkMiddleware from 'redux-thunk';
import { createStore, applyMiddleware } from 'redux';
import { fetchSubjects } from './actions';
import logger from './logger';
import rootReducer from './reducers';

import { Router, Route, IndexRoute, hashHistory } from "react-router";

import App from './Components/App';
import Subject from './Components/Subject';
import SubjectsList from './Components/SubjectsList';
import Test from './Components/Test';

const store = createStore(
	rootReducer,
	applyMiddleware(
		logger,
		thunkMiddleware
	)
);

store.dispatch(fetchSubjects());

const root = document.getElementById('root');

ReactDOM.render(
	<Provider store={store}>
		<Router history={hashHistory}>
			<Route path="/" component={App} >
				<IndexRoute component={SubjectsList} />
				<Route path="subject" component={Subject} />
				<Route path="test" component={Test} />
			</Route>
		</Router>
	</Provider>,
	root
);