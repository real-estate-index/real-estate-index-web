
// svg파일 기반으로 지도를 불라오고, 서울 인천 지역 외에는 현재 기능 지원이 불가해서 에러메시지를 출력하고,
// 서울 인천 지역을 클릭하면 해당 지역의 데이터를 불러와 출력하는 컴포넌트

// 기능 검증 필요

import React, { useState, useEffect } from 'react';
import axios from 'axios';

function MapComponent() {
  const [regionData, setRegionData] = useState(null);
  const [errorMessage, setErrorMessage] = useState('');

  useEffect(() => {
    fetch('/images/modified_country_light_purple.svg')
      .then(response => response.text())
      .then(svgData => {
        document.getElementById('svg-container').innerHTML = svgData;
        attachClickHandlers();
      });
  }, []);

  const attachClickHandlers = () => {
    document.querySelectorAll('path').forEach(path => {
      path.addEventListener('click', () => {
        if (path.id === 'seoul' || path.id === 'incheon') {
          fetchRegionData(path.id);
        } else {
          setErrorMessage('현재 지원되지 않는 기능입니다.');
          setRegionData(null); // 이전 지역 데이터 클리어
        }
      });
    });
  };

  const fetchRegionData = (regionId) => {
    axios.get(`/api/region/${regionId}`)
      .then(response => {
        setRegionData(response.data);
        setErrorMessage(''); // 에러 메시지 클리어
      })
      .catch(error => {
        console.error('Error fetching region data:', error);
        setErrorMessage('데이터를 불러오는 데 실패했습니다.');
      });
  };

  return (
    <div>
      <div id="svg-container"></div>
      {errorMessage && <p>{errorMessage}</p>}
      {regionData && (
        <div>
          <h2>Region Details</h2>
          <p>{regionData.name}: {regionData.indexValue}</p>
        </div>
      )}
    </div>
  );
}

export default MapComponent;