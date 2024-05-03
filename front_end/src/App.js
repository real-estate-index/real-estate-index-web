import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Map from './components/Map';
import FearGreedIndex from './components/FearGreedIndex';
import RegionDetails from './components/RegionDetails';
import Graph from './components/Graph';
import NewsAndIssues from './components/NewsAndIssues';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <h1>Real Estate Index</h1>
        </header>
        <main>
          <div className="dashboard">
            <FearGreedIndex />
            <Map />
            <RegionDetails />
            <NewsAndIssues />
            <Graph title="Graph1" />
            <Graph title="Graph2" />
          </div>
        </main>
      </div>
    </Router>
  );
}

export default App;
