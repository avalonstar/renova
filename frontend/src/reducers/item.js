import * as actions from 'actions/items';

const active = (state = {}, action) => {
  switch (action.type) {
    case actions.ITEM_FETCH.REQUEST:
      return { ...state, isFetching: true };
    case actions.ITEM_FETCH.SUCCESS:
      return { ...state, isFetching: false, ...action.response.entities.items };
    case actions.ITEM_FETCH.FAILURE:
      return { ...state, isFetching: false, error: action.error };
    default:
      return state;
  }
};

export default active;

export const getItem = (state, id) => state.active[id];
