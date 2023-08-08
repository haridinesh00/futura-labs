import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import AddData from "./AddData";
import DispData from "./DispData";
import UpdateData from "./UpdateData";
import reportWebVitals from "./reportWebVitals";
import NavigationBar from "./NavigationBar";
import WelcomePage from "./WelcomePage";
import { BrowserRouter, Route, Routes } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <BrowserRouter>
    <NavigationBar />
    <Routes>
      <Route path="" element={<WelcomePage />} />
      <Route path="/page1" element={<AddData />} />
      <Route path="/page2" element={<DispData />} />
      <Route path="/page3" element={<UpdateData />} />
    </Routes>
    {/* <Arlist1 /> */}
  </BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
