import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { Route, Switch } from 'react-router-dom';
import { ConnectedRouter } from 'react-router-redux';

import { ThemeProvider } from 'styled-components';

import App from 'containers/App';
import { Items } from 'containers/Database';
import { Dashboard } from 'layouts';
import baseStyles, { foundation } from 'helpers/foundation';

import store, { history } from './store';
import registerServiceWorker from './registerServiceWorker';

const RouteWithLayout = ({ layout, component, ...rest }) => (
  <Route
    {...rest}
    render={props =>
      React.createElement(layout, props, React.createElement(component, props))
    }
  />
);

const render = () => {
  baseStyles();
  ReactDOM.render(
    <Provider store={store}>
      <ConnectedRouter history={history}>
        <ThemeProvider theme={foundation}>
          <Switch>
            <RouteWithLayout
              layout={Dashboard}
              component={Items}
              path="/database/items"
            />
            <RouteWithLayout layout={Dashboard} component={App} />
          </Switch>
        </ThemeProvider>
      </ConnectedRouter>
    </Provider>,
    document.getElementById('root')
  );
};

render();
registerServiceWorker();
