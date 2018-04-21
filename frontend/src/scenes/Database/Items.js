import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

import { itemListFetch } from 'actions/items';
import { getItems } from 'reducers';

const propTypes = {
  request: PropTypes.func.isRequired,
  items: PropTypes.arrayOf(PropTypes.object)
};

const defaultProps = {
  items: []
};

class Items extends Component {
  componentDidMount() {
    this.props.request();
  }

  render() {
    // const { isFetching } = this.props;
    // if (isFetching && ) {
    //  return <p>loading...</p>
    // }
    return (
      <div>
        {/* {this.props.items.map(item => (
          <div key={item.id}>
            <small>{JSON.stringify(item)}</small>
          </div>
        ))} */}
      </div>
    );
  }
}

Items.propTypes = propTypes;
Items.defaultProps = defaultProps;

const mapStateToProps = state => ({
  items: getItems(state)
  // isFetching: getIsFetching(state)
});

export default connect(mapStateToProps, { request: itemListFetch.request })(
  Items
);
