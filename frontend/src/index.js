import React from 'react';
import ReactDOM from 'react-dom';

import { ThemeProvider } from 'styled-components';

import baseStyles, { foundation } from 'helpers/foundation';

import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';

const render = () => {
  baseStyles();
  ReactDOM.render(
    <ThemeProvider theme={foundation}>
      <App />
    </ThemeProvider>,
    document.getElementById('root')
  );
}

render();
registerServiceWorker();
