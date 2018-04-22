import * as fromItems from 'reducers/items';
import * as fromItem from 'reducers/item';

export const getItems = state => fromItems.getItems(state.items);

export const getItem = (state, id) => fromItem.getItem(state.items, id);
