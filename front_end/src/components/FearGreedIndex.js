import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './FearGreedIndex.css';

function FearGreedIndex() {
  const [indexData, setIndexData] = useState(null);

  useEffect(() => {
    axios.get('/api/fear-greed-index')
      .then(response => {
        setIndexData(response.data);
      })
      .catch(error => console.error('Error fetching Fear & Greed Index data:', error));
  }, []);

  const getBarColor = (value, index) => {
    const lowerBound = (4 - index) * 20;
    const upperBound = lowerBound + 20;
    return value >= lowerBound && value < upperBound;
  };

  const getIndicatorPosition = (value) => {
    if (value == 100) value =99;
    const lowerBound = -40 + Math.floor(value / 20) * 73.7;
    const location = (value % 20) / 20 * 68 + lowerBound;
    return `${location}px`;
  };

  return (
    <div>
      <h2 className="text-style">Fear & Greed Index</h2>
      <div className="content">
        {indexData ? (
          <div className="bar-wrapper">
            {[0, 1, 2, 3, 4].map((value, index) => (
              <div className="bar-container" key={index}>
                <div className={getBarColor(indexData.value_item, index) ? 'bar-filled' : 'bar'} />
              </div>
            ))}
          </div>
        ) : (
          <p>Loading...</p>
        )}
        {indexData && (
          <div className="indicator" style={{ bottom: getIndicatorPosition(indexData.value_item) }}>
            <div className="triangle" />
            <div className="circle" />
            <div className="circle2">
              <span>{indexData.value_item}</span>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default FearGreedIndex;
