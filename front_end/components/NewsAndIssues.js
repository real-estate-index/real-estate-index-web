// 예시 코드 - 프론트 미구현

import React, { useEffect, useState } from 'react';
import axios from 'axios';

function NewsAndIssues() {
  const [newsAndIssues, setNewsAndIssues] = useState([]);

  useEffect(() => {
    axios.get('/api/news_issues')
      .then(response => {
        setNewsAndIssues(response.data);
      })
      .catch(error => {
        console.error('Error fetching news and issues:', error);
      });
  }, []);

  return (
    <div className="news-and-issues">
      <h2>News & Issues</h2>
      <ul>
        {newsAndIssues.map(item => (
          <li key={item.title}>{item.title}</li>
        ))}
      </ul>
    </div>
  );
}
export default NewsAndIssues;