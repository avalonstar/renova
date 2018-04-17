import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

import { itemListFetch } from 'actions/items';
import * as selectors from 'selectors';

const propTypes = {
  request: PropTypes.func.isRequired,
  randomItems: PropTypes.arrayOf(PropTypes.object)
};

const defaultProps = {
  randomItems: []
};

class Items extends Component {
  componentDidMount() {
    this.props.request();
  }

  render() {
    return (
      <div>
        {this.props.randomItems.map(item => (
          <small>{JSON.stringify(item)}</small>
        ))}
      </div>
    );
  }
}

Items.propTypes = propTypes;
Items.defaultProps = defaultProps;

const mapStateToProps = state => ({
  randomItems: selectors.getRandomItems(state)
});

const mapDispatchToProps = dispatch => ({
  request: () => dispatch(itemListFetch.request())
});

export default connect(mapStateToProps, mapDispatchToProps)(Items);
