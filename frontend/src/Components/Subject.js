import React from 'react';
import { connect } from 'react-redux';
import { hashHistory, Link } from 'react-router';
import { staticTestSelected } from '../actions';

class Subject extends React.Component {
	componentWillMount() {
		const { store } = this.props;
		const { selectedSubject } = store;
		const { isSelected } = selectedSubject;
		if (isSelected === false) {
			hashHistory.push('');
		}
	}
	handleStaticTestClick(testId, subject) {
		// TODO: start from here.
		console.log(testId, subject);
	}
	render() {
		const { store } = this.props;
		const { selectedSubject } = store;
		const { queryName: subjectQueryName, name: subjectName } = selectedSubject;
		const { isFetching: staticTestsAreFetching } = store.staticTests;
		const staticTests = store.staticTests.tests.map(test =>
			<Link
				to="test"
				className="variant"
				key={test.id}
				onClick={this.handleStaticTestClick.bind(this, test.id, subjectQueryName)}
			>Вариант {test.number}</Link>
		)
		return (
			<div>
				<h2>{subjectName}</h2>
				{ staticTestsAreFetching &&
					<p>Подождите, идёт загрузка вариантов...</p>
				}
				{staticTests}
			</div>
		);
	}
}

function mapStateToProps (state) {
	return { store: state };
};

export default connect(mapStateToProps)(Subject);