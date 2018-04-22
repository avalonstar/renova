import { action, createRequestTypes } from './utils';

export const ITEM_LIST_FETCH = createRequestTypes('ITEM_LIST_FETCH');
export const ITEM_FETCH = createRequestTypes('ITEM_FETCH');

export const itemListFetch = {
  request: () => action(ITEM_LIST_FETCH.REQUEST),
  success: response => action(ITEM_LIST_FETCH.SUCCESS, { response }),
  failure: error => action(ITEM_LIST_FETCH.FAILURE, { error })
};

export const itemFetch = {
  request: id => action(ITEM_FETCH.REQUEST, { id }),
  success: (id, response) => action(ITEM_FETCH.SUCCESS, { id, response }),
  failure: (id, error) => action(ITEM_FETCH.FAILURE, { id, error })
};
