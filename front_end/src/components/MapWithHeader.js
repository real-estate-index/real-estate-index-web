import React, { useState } from 'react';
import MapComponent from './MapComponent';
import './MapWithHeader.css';

function MapWithHeader() {
  const [errorMessage, setErrorMessage] = useState('');

  return (
    <div className="map-wrapper">
      <div className="header">
        <h2 className="text-style">지역별 지표 조회</h2>
      </div>
      <MapComponent setErrorMessage={setErrorMessage} />
      {errorMessage && <div className="error-container"><p className="error-message">{errorMessage}</p></div>}
    </div>
  );
}

export default MapWithHeader;
