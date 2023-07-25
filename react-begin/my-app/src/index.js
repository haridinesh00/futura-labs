import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import New from './New_app';
import Card_eg from './Card_eg';
import Bootcard from './Bootcard';
import Array from './Array';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    {/* <App />
    <New />
    <Card_eg /> */}
    <Bootcard />
    {/* <Array /> */}
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
