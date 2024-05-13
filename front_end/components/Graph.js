// 프론트 미구현

import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import axios from 'axios';

function Graph({ title }) {
  const [chartData, setChartData] = useState({});

  useEffect(() => {
    axios.get(`/api/graph?title=${title}`)
      .then(response => {
        setChartData(response.data);
      })
      .catch(error => {
        console.error('Error fetching graph data:', error);
      });
  }, [title]);

  return (
    <div className="graph">
      <h2>{title}</h2>
      <Line data={chartData} />
    </div>
  );
}
export default Graph;