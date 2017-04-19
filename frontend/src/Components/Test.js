import React from 'react';
import { connect } from 'react-redux';

class Test extends React.Component {
	render() {
		return (
			<div>
				this is a test!
			</div>
		);
	}
}

function mapStateToProps (state) {
	return { store: state };
};

export default connect(mapStateToProps)(Test);