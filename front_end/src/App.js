import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './components/Home';
import Regions from './components/Regions';
import News from './components/News';
import Issues from './components/Issues';
import Graph from './components/Graph';

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/regions" component={Regions} />
        <Route path="/news" component={News} />
        <Route path="/issues" component={Issues} />
        <Route path="/graph" component={Graph} />
      </Switch>
    </Router>
  );
}

export default App;