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
    <div>
      <h1>Fear & Greed Index</h1>
      {indexData ? <p>Index Value: {indexData.value}</p> : <p>Loading...</p>}
    </div>
  );
}

export default FearGreedIndex;
