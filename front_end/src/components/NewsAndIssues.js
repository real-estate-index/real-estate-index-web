import React, { useState, useEffect } from 'react';

function NewsAndIssues() {
  const [news, setNews] = useState([]);
  const [issues, setIssues] = useState([]);
  const [activeCategory, setActiveCategory] = useState('news'); // 활성화된 카테고리를 추적하는 상태 변수

  useEffect(() => {
    // Django에서 제공하는 API 엔드포인트
    const apiUrl = '/api/news-and-issues';

    // 데이터를 가져오는 함수
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

    // 데이터 가져오기
    fetchData();
  }, []);

  const handleCategoryClick = (category) => {
    setActiveCategory(category);
  };

  const handleItemClick = (link) => {
    window.open(link, '_blank'); // 새 탭에서 링크 열기
  };

  return (
    <div className="rectangle">
      <h2 className="text-style">News & Issues</h2>
      <div className="content">
        <div>
          <h3>뉴스</h3>
          <button onClick={() => handleCategoryClick('news')}>뉴스 보기</button>
          {activeCategory === 'news' && (
            <ul>
              {news.map((item, index) => (
                <li key={index}>
                  <button onClick={() => handleItemClick(item.link)}>{item.title}</button>
                </li>
              ))}
            </ul>
          )}
        </div>
        <div>
          <h3>다음 이슈</h3>
          <button onClick={() => handleCategoryClick('issues')}>다음 이슈 보기</button>
          {activeCategory === 'issues' && (
            <ul>
              {issues.map((item, index) => (
                <li key={index}>
                  <button onClick={() => handleItemClick(item.link)}>{item.title}</button>
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </div>
  );
}

export default NewsAndIssues;
