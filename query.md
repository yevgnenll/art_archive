## 3. 다음 작업을 수행하는 SQL query들과 해당 리턴값을 작성해주시기 바랍니다.

* **주어진 artists, images 테이블 분석**


테이블 분석: artists

| column name | attribute |
| ------------- | ------------- |
| id  | not null && auto increment  |
| name  | 예술가의 이름 |
| birth_year  | 예술가의 출생연도  |
| death_year  | 예술가의 사망연도  |
| country  | 예술가의 국가  |
| genre | 예술가의 장르  |



테이블 분석: images 

artist_id는 artists테이블의 ForeignKey로 정의됨.

| column name | attribute |
| ------------- | ------------- |
| id  | not null && auto increment  |
| image_url  | 이미지 링크  |
| title  | 작품제목  |
| year  | 작품 생성된 연도  |
| artist_id  | artists테이블의 FK  |
| description  | 작품 특성(유채 etc.)  |



