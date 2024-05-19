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
    <div className="rectangle">
      <h2 className="text-style">Region Details</h2>
      <div className="content">
        <ul>
          {regionDetails.map(detail => (
            <li key={detail.name}>{detail.name}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}
export default RegionDetails;
