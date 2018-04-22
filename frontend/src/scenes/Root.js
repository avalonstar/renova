import React, { Fragment } from 'react';
import { Provider } from 'react-redux';
import { Route, Switch } from 'react-router-dom';
import { ConnectedRouter } from 'react-router-redux';

import { ThemeProvider } from 'styled-components';

import App from 'scenes/App';
import Database from 'scenes/Database';
import { Helmet, RouteWithLayout } from 'components/Common';
import { Dashboard } from 'layouts';
import { foundation } from 'helpers/foundation';
import { history } from 'store';

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
