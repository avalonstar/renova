import { all, fork } from 'redux-saga/effects';

import itemSagas from './items';

export default function* rootSaga() {
  yield all([fork(itemSagas)]);
}
