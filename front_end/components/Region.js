import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Regions() {
  const [regions, setRegions] = useState([]);

  useEffect(() => {
    axios.get('/api/regions')
      .then(response => {
        setRegions(response.data);
      })
      .catch(error => {
        console.error('Error fetching regions:', error);
      });
  }, []);

  return (
    <div>
      <h2>Regions</h2>
      <ul>
        {regions.map(region => (
          <li key={region.name}>{region.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default Regions;
