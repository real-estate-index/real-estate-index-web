import React, { useState, useEffect } from 'react';
import axios from 'axios';

function RegionDetails({ selectedRegion, regionName }) {
  const [districts, setDistricts] = useState([]);

  useEffect(() => {
    if (selectedRegion) {
      axios.get(`/api/regions/districts?regionId=${selectedRegion}`)
        .then(response => {
          setDistricts(response.data);
        })
        .catch(error => {
          console.error('Error fetching district details:', error);
        });
    }
  }, [selectedRegion]);

  return (
    <div className="region-details">
      <h2 className="text-style">{regionName}의 구 목록</h2>
      <div className="content">
        <ul>
          {districts.map(district => (
            <li key={district.id}>{district.name}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default RegionDetails;
