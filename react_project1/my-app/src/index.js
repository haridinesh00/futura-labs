import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import Navigation from './Navigation';
import Carouselimg from './Carouselimg';
import ProductDetails from './ProductDetails';
import Counter from './Counter';
import Changestr from './Changestr';
import Tableboot from './Tableboot';
import Routenav from './Routenav';
import reportWebVitals from './reportWebVitals';
import Arlist1 from './Arlist1';
import Dummy1 from './Dummy1';
import Dummy2 from './Dummy2';
import Changecolor from './Changecolor';
import { BrowserRouter, Route, Routes } from 'react-router-dom'

const root = ReactDOM.createRoot(document.getElementById('root'));

  <BrowserRouter>
    {/* <Navigation /> */}
    {/* <Caroot.render(rouselimg /> */}
    {/* <ProductDetails /> */}
    {/* <Counter /> */}
    {/* <Changestr /> */}
    {/* <Tableboot /> */}
    <Routenav />
    <Changecolor />
    <Routes>
      <Route path='/page1' element={<Dummy1 />} />
      <Route path='/page2' element={<Dummy2 />} />
    </Routes>
    {/* <Arlist1 /> */}
  </BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
