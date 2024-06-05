import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './FearGreedIndex.css';

function FearGreedIndex({ selectedDistrict }) {
  const [indexValue, setIndexValue] = useState(null);

  useEffect(() => {
    const districtId = selectedDistrict || 1;  // 기본값을 1로 설정
    axios.get(`/api/fear_greed_index?districtId=${districtId}`)
      .then(response => {
        if (response.data.length > 0) {
          setIndexValue(response.data[0].index_value);  // 데이터의 첫 번째 항목을 사용
        } else {
          setIndexValue(null);  // 데이터가 없는 경우
        }
      })
      .catch(error => console.error('Error fetching Fear & Greed Index data:', error));
  }, [selectedDistrict]);

  const getBarClass = (value, index) => {
    const lowerBound = (4 - index) * 20;
    const upperBound = lowerBound + 20;
    return value >= lowerBound && value < upperBound ? `bar bar-${index} bar-filled` : `bar bar-${index}`;
  };

  const getIndicatorPosition = (value) => {
    if (value === 100) value = 99;
    const lowerBound = -40 + Math.floor(value / 20) * 73.7;
    const location = (value % 20) / 20 * 68 + lowerBound;
    return `${location}px`;
  };

  return (
    <div>
      <h2 className="text-style">Fear & Greed Index</h2>
      <div className="content">
        {indexValue !== null ? (
          <div className="bar-wrapper">
            {[0, 1, 2, 3, 4].map((value, index) => (
              <div className="bar-container" key={index}>
                <div className={getBarClass(indexValue, index)} />
              </div>
            ))}
          </div>
        ) : (
          <p>Loading...</p>
        )}
        {indexValue !== null && (
          <div className="indicator" style={{ bottom: getIndicatorPosition(indexValue) }}>
            <div className="triangle" />
            <div className="circle" />
            <div className="circle2">
              <span>{indexValue}</span>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default FearGreedIndex;
