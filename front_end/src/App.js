import React, { useState } from 'react';
import { Routes, Route } from 'react-router-dom';
import Map from './components/Map';
import FearGreedIndex from './components/FearGreedIndex';
import RegionDetails from './components/RegionDetails';
import Graph from './components/Graph';
import NewsAndIssues from './components/NewsAndIssues';
import './App.css';

function App() {
  const [selectedRegion, setSelectedRegion] = useState('1'); // 기본값 서울
  const [regionName, setRegionName] = useState('서울'); // 기본값 서울

  const handleRegionSelect = (regionId, regionName) => {
    setSelectedRegion(regionId);
    setRegionName(regionName);
  };

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
          <RegionDetails selectedRegion={selectedRegion} regionName={regionName} />
        </div>
        <div className="widget map">
          <Map onRegionSelect={handleRegionSelect} />
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
        <Route path="/map" element={<Map onRegionSelect={handleRegionSelect} />} />
        <Route path="/index" element={<FearGreedIndex />} />
        <Route path="/details" element={<RegionDetails selectedRegion={selectedRegion} regionName={regionName} />} />
        <Route path="/graph" element={<Graph />} />
        <Route path="/news" element={<NewsAndIssues />} />
      </Routes>
    </div>
  );
}

export default App;
