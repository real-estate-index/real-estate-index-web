
```terminal
# 가상 환경 생성
python -m venv venv

# 가상 환경 활성화
# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# 장고 설치
pip install django

```

### 프론트엔드 구성

front_end/
├── src/
│   ├── components/
│   │   ├── Map.js              # 한국 지도를 보여주는 컴포넌트
│   │   ├── FearGreedIndex.js   # Fear & Greed Index 보여주는 컴포넌트
│   │   ├── RegionDetails.js    # 선택된 지역의 세부 정보를 보여주는 컴포넌트
│   │   ├── Graph.js            # 그래프를 보여주는 컴포넌트
│   │   ├── NewsAndIssues.js    # 뉴스와 이슈를 보여주는 컴포넌트
│   ├── App.js                  # 주요 애플리케이션 컴포넌트
│   ├── index.js                # 애플리케이션 진입점
├── public/
│   ├── index.html              # 주요 HTML 파일
├── package.json                # 프로젝트 의존성과 스크립트