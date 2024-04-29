import React, { useEffect, useState } from 'react';
import axios from 'axios';

function News() {
  const [newsItems, setNewsItems] = useState([]);

  useEffect(() => {
    axios.get('/api/news')
      .then(response => {
        setNewsItems(response.data);
      })
      .catch(error => {
        console.error('Error fetching news:', error);
      });
  }, []);

  return (
    <div>
      <h2>News</h2>
      <ul>
        {newsItems.map(item => (
          <li key={item.title}>
            <strong>{item.title}</strong>
            <p>{item.content}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default News;