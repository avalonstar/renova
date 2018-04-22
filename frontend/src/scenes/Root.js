import React, { Fragment } from 'react';
import { Provider } from 'react-redux';
import { Route, Switch } from 'react-router-dom';
import { ConnectedRouter } from 'react-router-redux';

import { ThemeProvider } from 'styled-components';

import App from 'scenes/App';
import { Helmet } from 'components/Common';
import { Item, Items } from 'scenes/Database';
import { Dashboard } from 'layouts';
import { foundation } from 'helpers/foundation';
import { history } from 'store';

const RouteWithLayout = ({ layout, component, ...rest }) => (
  <Route
    {...rest}
    render={props =>
      React.createElement(layout, props, React.createElement(component, props))
    }
  />
);

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

const Main = () => (
  <Fragment>
    <Helmet />
    <Switch>
      <RouteWithLayout layout={Dashboard} exact path="/" component={App} />
      <Route path="/database" component={Database} />
    </Switch>
  </Fragment>
);

const Root = ({ store }) => (
  <Provider store={store}>
    <ConnectedRouter history={history}>
      <ThemeProvider theme={foundation}>
        <Main />
      </ThemeProvider>
    </ConnectedRouter>
  </Provider>
);

export default Root;
