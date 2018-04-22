import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

import { itemFetch } from 'actions/items';

import * as selectors from './selectors';

const propTypes = {
  request: PropTypes.func.isRequired,
  id: PropTypes.number.isRequired,
  item: PropTypes.object
};

class Item extends Component {
  componentDidMount() {
    const { id } = this.props;
    this.props.request(id);
  }

  render() {
    return (
      <div>
        This is a single item.
        {JSON.stringify(this.props.item)}
      </div>
    );
  }
}

Item.propTypes = propTypes;

const mapStateToProps = (state, { match }) => {
  const { id } = match.params;
  return {
    item: selectors.getItem(state, id),
    id: parseInt(id, 10)
  };
};

export default connect(mapStateToProps, { request: itemFetch.request })(Item);
