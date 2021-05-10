import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import {BrowserRouter as Router} from 'react-router-dom'
import './assets/css/tailwind.css'

ReactDOM.render(
  <Router>
    <React.StrictMode>
        <App />
    </React.StrictMode>
  </Router>,
  document.getElementById('root')
);

