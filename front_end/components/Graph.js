import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';

function Graph() {
  const [data, setData] = useState({});

  useEffect(() => {
    axios.get('/api/graph')
      .then(response => {
        // 데이터를 Chart.js에서 사용할 수 있는 형태로 가공합니다.
        const chartData = {
          labels: response.data.labels,
          datasets: [
            {
              label: 'Real Estate Index',
              data: response.data.values,
              borderColor: 'rgba(75, 192, 192, 1)',
              fill: false,
            },
          ],
        };
        setData(chartData);
      })
      .catch(error => {
        console.error('Error fetching graph data:', error);
      });
  }, []);

  return (
    <div>
      <h2>Real Estate Index Graph</h2>
      <Line data={data} />
    </div>
  );
}

export default Graph;