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
        if (path.id === 'seoul') {
          onRegionSelect('1', '서울');
        } else if (path.id === 'incheon') {
          onRegionSelect('2', '인천');
        } else {
          alert('현재 지원되지 않는 기능입니다.');
          onRegionSelect('1', '서울'); // 기본값 서울
        }
      });
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
      </div>
    </div>
  );
}

export default Map;
