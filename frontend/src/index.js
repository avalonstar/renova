import React from 'react';
import ReactDOM from 'react-dom';

import Root from 'containers/Root';
import baseStyles from 'helpers/foundation';

import configureStore from './store';
import registerServiceWorker from './registerServiceWorker';

const store = configureStore();

const render = () => {
  baseStyles();
  ReactDOM.render(<Root store={store} />, document.getElementById('root'));
};

render();
registerServiceWorker();
