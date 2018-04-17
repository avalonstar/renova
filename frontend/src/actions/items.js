import { action, createRequestTypes } from './utils';

export const ITEM_LIST_FETCH = createRequestTypes('ITEM_LIST_FETCH');
export const ITEM_FETCH = createRequestTypes('ITEM_FETCH');

export const itemListFetch = {
  request: () => action(ITEM_LIST_FETCH.REQUEST),
  success: payload => action(ITEM_LIST_FETCH.SUCCESS, { payload }),
  failure: error => action(ITEM_LIST_FETCH.FAILURE, { error })
};

export const itemFetch = {
  request: pk => action(ITEM_FETCH.REQUEST, { pk }),
  success: payload => action(ITEM_FETCH.SUCCESS, { payload }),
  failure: error => action(ITEM_FETCH.FAILURE, { error })
};
