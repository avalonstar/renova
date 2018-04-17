import axios from 'axios';

import { all, call, put, takeLatest } from 'redux-saga/effects';

import * as actions from 'actions/items';

const { itemListFetch, itemFetch } = actions;

function* fetchItem(pk) {
  try {
    const uri = `http://localhost:8000/api/items/${pk}`;
    const response = yield call(axios.get, uri);
    yield put(itemFetch.success(response.data));
  } catch (error) {
    yield put(itemFetch.failure());
  }
}

function* fetchItemList() {
  try {
    const uri = `http://localhost:8000/api/items/`;
    const response = yield call(axios.get, uri);
    yield put(itemListFetch.success(response.data));
  } catch (error) {
    yield put(itemListFetch.failure());
  }
}

export default function* itemSagas() {
  yield all([
    takeLatest(actions.ITEM_LIST_FETCH.REQUEST, fetchItemList),
    takeLatest(actions.ITEM_FETCH.REQUEST, fetchItem)
  ]);
}
