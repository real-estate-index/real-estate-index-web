import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'; // 전역 스타일 시트
import App from './App';
import { BrowserRouter } from 'react-router-dom'; // BrowserRouter 임포트

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);
