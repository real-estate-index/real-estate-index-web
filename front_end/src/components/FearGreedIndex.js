import React, { useState, useEffect } from 'react';
import axios from 'axios';

function FearGreedIndex() {
  const [indexData, setIndexData] = useState(null);

  useEffect(() => {
    axios.get('/api/fear-greed-index')
      .then(response => {
        setIndexData(response.data);
      })
      .catch(error => console.error('Error fetching Fear & Greed Index data:', error));
  }, []);

  return (
    <div className="rectangle">
      <h2 className="text-style">Fear & Greed Index</h2>
      <div className="content">
        {indexData ? <p>Index Value: {indexData.value}</p> : <p>Loading...</p>}
      </div>
    </div>
  );
}

export default FearGreedIndex;
