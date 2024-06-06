import React, { useState, useEffect } from 'react';
import './NewsAndIssues.css'; // 추가적인 CSS 스타일을 적용하기 위해 CSS 파일을 임포트합니다.

function NewsAndIssues() {
  const [news, setNews] = useState([]);
  const [issues, setIssues] = useState([]);
  const [activeCategory, setActiveCategory] = useState('news');

  useEffect(() => {
    const apiUrl = '/api/news_and_issues';

    const fetchData = async () => {
      try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        setNews(data.news);
        setIssues(data.issues);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  const handleCategoryClick = (category) => {
    setActiveCategory(category);
  };

  const handleItemClick = (link) => {
    window.open(link, '_blank');
  };

  return (
    <div className="news-and-issues">
      <h2 className="title">뉴스 & 정부 보도 자료</h2>
      <div className="category">
        <button
          className={`category-button ${activeCategory === 'news' ? 'active' : ''}`}
          onClick={() => handleCategoryClick('news')}
        >
          뉴스 보기
        </button>
        <button
          className={`category-button ${activeCategory === 'issues' ? 'active' : ''}`}
          onClick={() => handleCategoryClick('issues')}
        >
          정부 보도자료 보기
        </button>
      </div>
      <div className="content">
        {activeCategory === 'news' && (
          <ul className="list">
            {news.length === 0 ? (
              <li className="list-item">뉴스가 없습니다.</li>
            ) : (
              news.map((item, index) => (
                <li key={index} className="list-item">
                  <button onClick={() => handleItemClick(item.link)}>
                    <div className="title">{item.title}</div>
                    <div className="description">{item.description}</div>
                  </button>
                </li>
              ))
            )}
          </ul>
        )}
        {activeCategory === 'issues' && (
          <ul className="list">
            {issues.length === 0 ? (
              <li className="list-item">정부 보도자료가 없습니다.</li>
            ) : (
              issues.map((item, index) => (
                <li key={index} className="list-item">
                  <button onClick={() => handleItemClick(item.link)}>
                    <div className="title">{item.title}</div>
                  </button>
                </li>
              ))
            )}
          </ul>
        )}
      </div>
    </div>
  );
}

export default NewsAndIssues;
