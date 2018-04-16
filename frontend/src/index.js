import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { Route, Switch } from 'react-router-dom';
import { ConnectedRouter } from 'react-router-redux';

import { ThemeProvider } from 'styled-components';

import App from 'containers/App';
import baseStyles, { foundation } from 'helpers/foundation';

import store, { history } from './store';
import registerServiceWorker from './registerServiceWorker';

const render = () => {
  baseStyles();
  ReactDOM.render(
    <Provider store={store}>
      <ConnectedRouter history={history}>
        <ThemeProvider theme={foundation}>
          <Switch>
            <Route component={App} />
          </Switch>
        </ThemeProvider>
      </ConnectedRouter>
    </Provider>,
    document.getElementById('root')
  );
};

render();
registerServiceWorker();
