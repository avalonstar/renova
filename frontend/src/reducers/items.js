import { combineReducers } from 'redux';
import { createSelector } from 'reselect';

import * as actions from 'actions/items';

import active from './item';

const allIds = (state = [], action) => {
  if (action.response) {
    return [...action.response.result];
  }
  return state;
};

const byId = (state = {}, action) => {
  if (action.response) {
    return {
      ...state,
      ...action.response.entities.items
    };
  }
  return state;
};

const isFetching = (state = false, action) => {
  switch (action.type) {
    case actions.ITEM_LIST_FETCH.REQUEST:
      return true;
    case actions.ITEM_LIST_FETCH.SUCCESS:
    case actions.ITEM_LIST_FETCH.FAILURE:
      return false;
    default:
      return state;
  }
};

const items = combineReducers({
  byId,
  allIds,
  active,
  isFetching
});

export default items;

const getItemsById = state => state.byId;
const getAllIds = state => state.allIds;

export const getItems = createSelector(
  [getAllIds, getItemsById],
  (ids, entities) => ids.map(id => entities[id])
);

export const getErrorMessage = state => state.error;
export const getIsFetching = state => state.isFetching;
