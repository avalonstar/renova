import * as actions from 'actions/items';

const initialState = {};

const items = (state = initialState, action) => {
  switch (action.type) {
    case actions.ITEM_LIST_FETCH.REQUEST:
      return { ...state, isLoading: true };
    case actions.ITEM_LIST_FETCH.SUCCESS:
      return { ...state, isLoading: false, payload: action.payload };
    case actions.ITEM_LIST_FETCH.FAILURE:
      return { ...state, isLoading: false, isError: true };
    default:
      return state;
  }
};

export default items;
