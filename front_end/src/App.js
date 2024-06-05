import React, { useState } from 'react';
import { Routes, Route } from 'react-router-dom';
import Map from './components/Map';
import FearGreedIndex from './components/FearGreedIndex';
import RegionDetails from './components/RegionDetails';
import Graph1 from './components/Graph1';
import Graph2 from './components/Graph2';
import Graph3 from './components/Graph3';
import Graph4 from './components/Graph4';
import NewsAndIssues from './components/NewsAndIssues';
import './App.css';

function App() {
  const [selectedRegion, setSelectedRegion] = useState('1'); // 기본값 서울
  const [regionName, setRegionName] = useState('서울'); // 기본값 서울
  const [selectedDistrict, setSelectedDistrict] = useState(1); // 기본값 district_id 1

  const handleRegionSelect = (regionId, regionName) => {
    setSelectedRegion(regionId);
    setRegionName(regionName);
  };

  const handleDistrictSelect = (districtId) => {
    setSelectedDistrict(districtId);
  };

  return (
    <div className="page-layout">
      <header className="header">
        <h1 className="text-style">Real Estate Index</h1>
      </header>
      <div className="dashboard">
        <div className="widget fear-greed-index">
          <FearGreedIndex selectedDistrict={selectedDistrict} />
        </div>
        <div className="widget region-details">
          <RegionDetails selectedRegion={selectedRegion} regionName={regionName} onSelectDistrict={handleDistrictSelect} />
        </div>
        <div className="widget map">
          <Map onRegionSelect={handleRegionSelect} />
        </div>
        <div className="widget news-and-issues">
          <NewsAndIssues />
        </div>
        <div className="widget graph1">
          <Graph1 districtId={selectedDistrict} />
        </div>
        <div className="widget graph2">
          <Graph2 districtId={selectedDistrict} />
        </div>
        <div className="widget graph3">
          <Graph3 districtId={selectedDistrict} />
        </div>
        <div className="widget graph4">
          <Graph4 districtId={selectedDistrict} />
        </div>
      </div>
      <Routes>
        <Route path="/map" element={<Map onRegionSelect={handleRegionSelect} />} />
        <Route path="/index" element={<FearGreedIndex selectedDistrict={selectedDistrict} />} />
        <Route path="/details" element={<RegionDetails selectedRegion={selectedRegion} regionName={regionName} onSelectDistrict={handleDistrictSelect} />} />
        <Route path="/graph1" element={<Graph1 districtId={selectedDistrict} />} />
        <Route path="/graph2" element={<Graph2 districtId={selectedDistrict} />} />
        <Route path="/graph3" element={<Graph3 districtId={selectedDistrict} />} />
        <Route path="/graph4" element={<Graph4 districtId={selectedDistrict} />} />
        <Route path="/news" element={<NewsAndIssues />} />
      </Routes>
    </div>
  );
}

export default App;
