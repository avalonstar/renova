import React from 'react';
import { Switch } from 'react-router-dom';

import { Dashboard } from 'layouts';
import { RouteWithLayout } from 'components/Common';

import Item from './Item';
import Items from './Items';

const Database = () => (
  <Switch>
    <RouteWithLayout
      layout={Dashboard}
      component={Items}
      exact
      path="/database/items"
    />
    <RouteWithLayout
      layout={Dashboard}
      component={Item}
      path="/database/item/:id"
    />
  </Switch>
);

export default Database;
