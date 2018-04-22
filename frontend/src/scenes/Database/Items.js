import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';

import { itemListFetch } from 'actions/items';

import * as selectors from './selectors';

const propTypes = {
  request: PropTypes.func.isRequired
};

class Items extends Component {
  componentDidMount() {
    this.props.request();
  }

  render() {
    const { isFetching, items } = this.props;
    if (isFetching && items) {
      return <p>loading...</p>;
    }

    return (
      <div>
        {items.map(item => (
          <div key={item.id}>
            <Link to={`/database/item/${item.id}`}>
              <small>{JSON.stringify(item)}</small>
            </Link>
          </div>
        ))}
      </div>
    );
  }
}

Items.propTypes = propTypes;

const mapStateToProps = state => ({
  items: selectors.getItems(state)
  // isFetching: getIsFetching(state)
});

export default connect(mapStateToProps, { request: itemListFetch.request })(
  Items
);
