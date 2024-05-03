// 프론트 미구현

import React, { useState, useEffect } from 'react';
import axios from 'axios';

function RegionDetails() {
  const [regionDetails, setRegionDetails] = useState([]);

  useEffect(() => {
    axios.get('/api/region_details')
      .then(response => {
        setRegionDetails(response.data);
      })
      .catch(error => {
        console.error('Error fetching region details:', error);
      });
  }, []);

  return (
    <div className="region-details">
      <h2>Region Details</h2>
      <ul>
        {regionDetails.map(detail => (
          <li key={detail.name}>{detail.name}</li>
        ))}
      </ul>
    </div>
  );
}
export default RegionDetails;