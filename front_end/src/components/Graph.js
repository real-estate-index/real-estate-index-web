import React, { useEffect, useRef } from 'react';
import Chart from 'chart.js/auto';
import './Graph.css'; // 그래프 스타일을 위한 CSS 파일 임포트

function Graph() {
  const chartRef = useRef(null);

  useEffect(() => {
    const myChart = new Chart(chartRef.current, {
      type: 'line',
      data: {
        labels: ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"], // 이 부분은 실제 데이터에 맞게 조정 필요
        datasets: [{
          label: '심리지수',
          data: [65, 59, 80, 81, 56, 55, 40, 60, 70, 45, 30, 80, 95, 70, 50], // 또한 이 데이터도 실제 데이터로 교체 필요
          fill: false,
          borderColor: '#8E85FE',
          tension: 0.1
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false, // 크기를 유지하지 않도록 설정
      }
    });

    return () => myChart.destroy();
  }, []);

  return (
    <div className="rectangle">
      <h2 className="text-style">Graph1</h2>
      <div className="content">
        <canvas ref={chartRef} className="graph-canvas"></canvas>
      </div>
    </div>
  );
}

export default Graph;
