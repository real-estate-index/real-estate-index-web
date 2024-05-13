// App.js
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import About from './components/About';
import Map from './components/Map';  // 예제로 추가된 다른 컴포넌트
import FearGreedIndex from './components/FearGreedIndex';
import RegionDetails from './components/RegionDetails';
import Graph from './components/Graph';
import NewsAndIssues from './components/NewsAndIssues';

function App() {
  return (
    <Routes>
      <Route path="/map" element={<Map />} />
      <Route path="/index" element={<FearGreedIndex />} />
      <Route path="/details" element={<RegionDetails />} />
      <Route path="/graph" element={<Graph />} />
      <Route path="/news" element={<NewsAndIssues />} />
    </Routes>
  );
}

export default App;
