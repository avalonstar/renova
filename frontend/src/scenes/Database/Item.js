import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

import { itemFetch } from 'actions/items';
import { getItem } from 'reducers';

const propTypes = {
  request: PropTypes.func.isRequired,
  pk: PropTypes.number,
  item: PropTypes.object
};

class Item extends Component {
  componentDidMount() {
    const { pk } = this.props;
    this.props.request(pk);
  }

  render() {
    return (
      <div>
        This is a single item.
        {JSON.stringify(this.props)}
      </div>
    );
  }
}

Item.propTypes = propTypes;

const mapStateToProps = (state, { match }) => {
  const { pk } = match.params;
  return { item: getItem(state, pk), pk: parseInt(pk, 10) };
};

export default connect(mapStateToProps, { request: itemFetch.request })(Item);
