
![버전2](https://github.com/real-estate-index/real-estate-index-web/assets/99078115/bb4d12fd-0b03-4574-b1db-96c6358bea4e)

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

```
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
```

### 프론트엔드 실행하기

#### 1. npm 설치하기

아래 명령어를 입력하서 npm을 설치합니다.
```terminal
npm install --legacy-peer-deps
```

예시 성공화면은 아래와 같습니다.
```
npm WARN deprecated @types/recoil@0.0.9: This is a stub types definition. recoil provides its own type definitions, so you do not need this installed.
npm WARN deprecated @babel/plugin-proposal-class-properties@7.18.6: This proposal has been merged to the ECMAScript standard and thus this plugin is no longer maintained. Please use @babel/plugin-transform-class-properties instead.
npm WARN deprecated @babel/plugin-proposal-nullish-coalescing-operator@7.18.6: This proposal has been merged to the ECMAScript standard and thus this plugin is no longer maintained. Please use @babel/plugin-transform-nullish-coalescing-operator instead.
npm WARN deprecated @babel/plugin-proposal-private-methods@7.18.6: This proposal has been merged to the ECMAScript standard and thus this plugin is no longer maintained. Please use @babel/plugin-transform-private-methods instead.
npm WARN deprecated @babel/plugin-proposal-numeric-separator@7.18.6: This proposal has been merged to the ECMAScript standard and thus this plugin is no longer maintained. Please use @babel/plugin-transform-numeric-separator instead.
npm WARN deprecated @babel/plugin-proposal-optional-chaining@7.21.0: This proposal has been merged to the ECMAScript standard and thus this plugin is no longer maintained. Please use @babel/plugin-transform-optional-chaining instead.
npm WARN deprecated stable@0.1.8: Modern JS already guarantees Array#sort() is a stable sort, so this library is deprecated. See the compatibility table on MDN: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#browser_compatibility
npm WARN deprecated rollup-plugin-terser@7.0.2: This package has been deprecated and is no longer maintained. Please use @rollup/plugin-terser     
npm WARN deprecated domexception@2.0.1: Use your platform's native DOMException instead
npm WARN deprecated abab@2.0.6: Use your platform's native atob() and btoa() methods instead
npm WARN deprecated sourcemap-codec@1.4.8: Please use @jridgewell/sourcemap-codec instead
npm WARN deprecated w3c-hr-time@1.0.2: Use your platform's native performance.now() and performance.timeOrigin.
npm WARN deprecated workbox-cacheable-response@6.6.0: workbox-background-sync@6.6.0
npm WARN deprecated workbox-google-analytics@6.6.0: It is not compatible with newer versions of GA starting with v4, as long as you are using GAv3 it should be ok, but the package is not longer being maintained
npm WARN deprecated svgo@1.3.2: This SVGO version is no longer supported. Upgrade to v2.x.x.

added 1439 packages, and audited 1647 packages in 2m

274 packages are looking for funding
  run `npm fund` for details

8 vulnerabilities (2 moderate, 6 high)

To address all issues (including breaking changes), run:
  npm audit fix --force

Run `npm audit` for details.
```

#### 2. npm 실행하기

1. npm은 front_end 폴더 위치에서 실행해야 합니다.

    ```
    cd front_end
    ```
  
2. 이후 프론트 서버를 실행하기 위해 터미널에 아래 명령어를 입력합니다.

    ```
    npm start
    ```
