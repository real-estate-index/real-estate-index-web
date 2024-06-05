import React, { useEffect, useRef } from 'react';
import './Map.css';

function Map({ onRegionSelect }) {
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
        switch (path.id) {
          case 'seoul':
            onRegionSelect('1', '서울');
            break;
          case 'incheon':
            onRegionSelect('2', '인천');
            break;
          // Add more cases for other regions if needed
          default:
            alert('현재 지원되지 않는 기능입니다.');
        }
      });
    });
  };

  const centerMap = () => {
    const container = containerRef.current;
    if (container) {
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
      </div>
    </div>
  );
}

export default Map;
