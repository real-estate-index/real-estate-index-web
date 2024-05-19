import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Map from './components/Map';
import FearGreedIndex from './components/FearGreedIndex';
import RegionDetails from './components/RegionDetails';
import Graph from './components/Graph';
import NewsAndIssues from './components/NewsAndIssues';
import './App.css'; // App.css로 스타일 시트 임포트

function App() {
  return (
    <div className="page-layout">
      <header className="header">
        <h1 className="text-style">Real Estate Index</h1>
      </header>
      <div className="dashboard">
        <div className="widget fear-greed-index">
          <FearGreedIndex />
        </div>
        <div className="widget region-details">
          <RegionDetails />
        </div>
        <div className="widget map">
          <Map />
        </div>
        <div className="widget news-and-issues">
          <NewsAndIssues />
        </div>
        <div className="widget graph1">
          <Graph />
        </div>
        <div className="widget graph2">
          <Graph />
        </div>
      </div>
      <Routes>
        <Route path="/map" element={<Map />} />
        <Route path="/index" element={<FearGreedIndex />} />
        <Route path="/details" element={<RegionDetails />} />
        <Route path="/graph" element={<Graph />} />
        <Route path="/news" element={<NewsAndIssues />} />
      </Routes>
    </div>
  );
}

export default App;
