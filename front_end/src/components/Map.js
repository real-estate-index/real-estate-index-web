import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import './Map.css';

function Map() {
  const [regionData, setRegionData] = useState(null);
  const containerRef = useRef(null);

  useEffect(() => {
    fetch('/images/korea_map.svg')
      .then(response => response.text())
      .then(svgData => {
        document.getElementById('svg-container').innerHTML = svgData;
        attachClickHandlers();
        centerMap();
      });
  }, []);

  const attachClickHandlers = () => {
    document.querySelectorAll('path').forEach(path => {
      path.addEventListener('click', () => {
        if (path.id === 'seoul' || path.id === 'incheon') {
          fetchRegionData(path.id);
        } else {
          alert('현재 지원되지 않는 기능입니다.');
          setRegionData(null); // 이전 지역 데이터 클리어
        }
      });
    });
  };

  const fetchRegionData = (regionId) => {
    axios.get(`/api/region/${regionId}`)
      .then(response => {
        setRegionData(response.data);
      })
      .catch(error => {
        console.error('Error fetching region data:', error);
        alert('데이터를 불러오는 데 실패했습니다.');
      });
  };

  const centerMap = () => {
    const container = containerRef.current;
    if (container) {
      // 지도 중앙에 고정할 좌표
      const fixedX = 550; 
      const fixedY = 550; 
      container.scrollLeft = fixedX - container.clientWidth / 2;
      container.scrollTop = fixedY - container.clientHeight / 2;
    }
  };

  return (
    <div className="map-container">
      <div className="title-container">
        <h2 className="text-style">지역별 지표 조회</h2>
      </div>
      <div className="rectangle" ref={containerRef}>
        <div className="content">
          <div id="svg-container"></div>
        </div>
        {regionData && (
          <div className="region-details">
            <h2>Region Details</h2>
            <p>{regionData.name}: {regionData.indexValue}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default Map;
