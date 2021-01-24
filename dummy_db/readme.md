# Dummy DB
프론트엔드/백엔드 간의 원활한 연동을 위하여 데이터 베이스 구조를 설계했습니다.
더미 데이터를 만드는 데 사용한 jupyter notebook 파일을 첨부합니다. 참고하시기 바랍니다.

## 기본 구조 및 참고 사항
sql 데이터베이스에 dictionary파일을 저장하기 위해 json을 형식을 이용하였습니다.
.db 파일은 StockDB, IssueDB, NewsDB 세 개의 테이블로 구성됩니다.
각 테이블에 있는 data 항목은 <ins>json.loads()를 이용해 dictionary로 변환</ins>하여 사용할 수 있습니다.
그리고 <ins>datetime.datetime.strptime()을 이용해 날짜를 인식</ins>할 수 있습니다.

## StockDB
```
StockDB  # SQL Table
├── stock_id  # int, 종목의 고유 번호
├── name  # text, 종목 이름
└── data  # dict
    ├── stock_id  # int, 위 항목과 같음
    ├── name  # str, 위 항목과 같음
    └── issues  # list, 종목 이슈들의 issue_id 나열
```

## IssueDB
```
IssueDB  # SQL Table
├── issue_id  # int, 이슈의 고유 번호
├── issue  # text, 이슈를 대표하는 문장
└── data  # dict
    ├── issue_id  # int, 위 항목과 같음
    ├── issue  # str, 위 항목과 같음
    ├── date_i  # str, 이슈의 최초 뉴스 날짜, '%Y-%m-%d' 형식
    ├── date_f  # str, 이슈의 최근 뉴스 날짜, '%Y-%m-%d' 형식
    └── news  # list, 이슈를 구성하는 뉴스들의 news_id 나열
```

## NewsDB
```
NewsDB  # SQL Table
├── news_id  # int, 뉴스의 고유 번호
└── data  # dict
    ├── news_id  # int, 위 항목과 같음
    ├── title  # str, 뉴스 제목
    ├── date  # str, 뉴스 업로드 날짜, '%Y-%m-%d' 형식
    ├── text  # str, 기사 요약
    └── url  # str
```
