# 오랜 All:N

## 준비
'''
git clone https://github.com/jsheo96/AllN.git

cd AllN

pip install -r requirements.txt
'''

## 로컬DB와 서버DB 동기화
'''
python manage.py migrate 
'''

## 개발 서버 실행
'''
python manage.py runserver /*0:8000*/
'''

## 개발 중인 페이지 확인
http://localhost:8000/stock

## News Database 이용 방법

http://jsheo96.iptime.org:8888/stock/database
에 들어가서 news.db를 AllN 폴더에 다운받기

python db_reader.py로 news.db 안의 데이터 읽어보기
