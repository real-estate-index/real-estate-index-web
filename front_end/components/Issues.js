import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Issues() {
  const [issues, setIssues] = useState([]);

  useEffect(() => {
    axios.get('/api/issues')
      .then(response => {
        setIssues(response.data);
      })
      .catch(error => {
        console.error('Error fetching issues:', error);
      });
  }, []);

  return (
    <div>
      <h2>Issues</h2>
      <ul>
        {issues.map(issue => (
          <li key={issue.title}>
            <strong>{issue.title}</strong>
            <p>{issue.content}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Issues;