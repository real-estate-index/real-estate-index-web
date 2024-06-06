import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './RegionDetails.css';

function RegionDetails({ selectedRegion, regionName, onSelectDistrict }) {
  const [districts, setDistricts] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 8;

  useEffect(() => {
    if (selectedRegion) {
      axios.get(`/api/region_districts?regionId=${selectedRegion}`)
        .then(response => {
          setDistricts(response.data);
          setCurrentPage(1); // Reset to first page on region change
        })
        .catch(error => {
          console.error('Error fetching district details:', error);
        });
    }
  }, [selectedRegion]);

  const handleDistrictClick = (event, districtId) => {
    event.preventDefault();
    onSelectDistrict(districtId);
  };

  const handlePageChange = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  const startIndex = (currentPage - 1) * itemsPerPage;
  const currentDistricts = districts.slice(startIndex, startIndex + itemsPerPage);
  const totalPages = Math.ceil(districts.length / itemsPerPage);

  return (
    <div className="region-details">
      <div className="text-style-container">
        <h2 className="text-style">{regionName}의 구 목록</h2>
      </div>
      <div className="button-container">
        {currentDistricts.map(district => (
          <button 
            key={district.id} 
            className="district-button" 
            onClick={(e) => handleDistrictClick(e, district.id)}
          >
            {district.name}
          </button>
        ))}
      </div>
      <div className="pagination">
        {Array.from({ length: totalPages }, (_, index) => (
          <button 
            key={index + 1} 
            className={`page-button ${currentPage === index + 1 ? 'active' : ''}`} 
            onClick={() => handlePageChange(index + 1)}
          >
            {index + 1}
          </button>
        ))}
      </div>
    </div>
  );
}

export default RegionDetails;
