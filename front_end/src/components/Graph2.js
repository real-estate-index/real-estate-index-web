import React, { useEffect, useRef } from 'react';
import Chart from 'chart.js/auto';
import './Graph.css'; // 그래프 스타일을 위한 CSS 파일 임포트

function Graph2({ districtId }) {
  const chartRef = useRef(null);
  const myChartRef = useRef(null); // 차트를 저장할 Ref

  useEffect(() => {
    const fetchData = async () => {
      if (districtId) {
        // 이전 차트를 파괴합니다.
        if (myChartRef.current) {
          myChartRef.current.destroy();
        }

        const response = await fetch(`/api/trade_price?district_id=${districtId}`);
        const data = await response.json();
        const labels = data.map(item => item.year_month);
        const values = data.map(item => item.price);

        // 새로운 차트를 생성하고 Ref에 저장합니다.
        myChartRef.current = new Chart(chartRef.current, {
          type: 'line',
          data: {
            labels: labels,
            datasets: [{
              label: '평당 거래가',
              data: values,
              fill: false,
              borderColor: '#8E85FE',
              tension: 0.1
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
          }
        });
      }
    };

    fetchData();

    // 컴포넌트가 언마운트될 때 차트를 파괴합니다.
    return () => {
      if (myChartRef.current) {
        myChartRef.current.destroy();
      }
    };
  }, [districtId]);

  return (
    <div className="rectangle">
      <h2 className="text-style">평당 거래가</h2>
      <div className="content">
        <canvas ref={chartRef} className="graph-canvas"></canvas>
      </div>
    </div>
  );
}

export default Graph2;
