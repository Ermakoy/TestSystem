import React from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router';
import { subjectSelected, fetchStaticTests } from '../actions';

class SubjectsList extends React.Component {
	handleSubjectClick(queryName, name) {
		const { dispatch } = this.props;
		dispatch(subjectSelected(queryName, name));
		dispatch(fetchStaticTests(queryName));
	}
	render() {
		const { store } = this.props;
		const {subjectsList } = store;
		const isFetching = subjectsList.isFetching;
		const subjects = subjectsList.subjects.map((subject, i) => 
			<Link 
				onClick={this.handleSubjectClick.bind(this, subject.nameQuery, subject.name)}
				to='subject'
				key={i}
			>
				{subject.name}
			</Link>
		);
		return (
			<div>
				<h2>Выберите предмет</h2>
				{ isFetching &&
					<p>Подождите, идёт загрузка предметов...</p>
				}
				<div className="subjects">
					{subjects}
				</div>
			</div>
		);
	}
}

function mapStateToProps (state) {
	return { store: state };
};

export default connect(mapStateToProps)(SubjectsList);