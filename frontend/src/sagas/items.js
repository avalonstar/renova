import axios from 'axios';
import { normalize } from 'normalizr';
import { all, call, put, takeLatest } from 'redux-saga/effects';

import * as schema from 'actions/schema';
import * as actions from 'actions/items';

const { itemListFetch, itemFetch } = actions;

function* fetchItem(item) {
  try {
    const uri = `http://localhost:8000/api/items/${item.pk}`;
    const response = yield call(axios.get, uri);
    yield put(itemFetch.success(normalize(response.data, schema.item)));
  } catch (error) {
    yield put(itemFetch.failure(error));
  }
}

function* fetchItemList() {
  try {
    const uri = `http://localhost:8000/api/items/`;
    const response = yield call(axios.get, uri);
    yield put(itemListFetch.success(normalize(response.data, schema.itemList)));
  } catch (error) {
    yield put(itemListFetch.failure(error));
  }
}

export default function* itemSagas() {
  yield all([
    takeLatest(actions.ITEM_LIST_FETCH.REQUEST, fetchItemList),
    takeLatest(actions.ITEM_FETCH.REQUEST, fetchItem)
  ]);
}
