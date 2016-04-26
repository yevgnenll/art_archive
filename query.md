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


----------

### 1. '제니 오델' 이라는 name을 가진 image의 title 가져오기
    
**답안**: 쓰레기 셀카


<pre>
SELECT
	art.*, img.*
FROM
	artists as art
LEFT JOIN images AS img
	on art.`id` = img.artist_id
WHERE
	art.name="제니 오델";
</pre>

이 쿼리로 처음 확인을 하였고 답안은 아래와 같습니다.

<pre>
SELECT
	img.title
FROM
	artists as art
LEFT JOIN images AS img
	on art.`id` = img.artist_id
WHERE
	art.name="제니 오델";
</pre>

작품 제목만을 찾는 쿼리입니다.

--------


### 2. 인상주의 artist의 3개의 이미지 가져오기

**답안**:


<pre>
    http://www.gulbenkian.pt/prjdir/gulbenkian/images/mediaRep/museu/colecao/pintura/Inv._2361Trat.jpg
    http://www.manet.org/images/gallery/the-luncheon-on-the-grass.jpg
    http://mfas3.s3.amazonaws.com/objects/SC232880.jpg
</pre>

1번의 정답과 같이 처음엔 모든 데이터를 확인하기 위해 아래와 같이 만들었습니다

<pre>
SELECT
	art.*, img.*
FROM
	artists as art
LEFT JOIN images AS img
	on art.`id` = img.artist_id
WHERE
	art.genre = "인상주의"
</pre>

결과는 7명의 예술가와 12개의 작품이 나왔습니다. 하지만 문제에서 별도의 기준이 없어 아래와 같이 작성하였습니다.


<pre>
SELECT
	img.image_url
FROM
	artists as art
LEFT JOIN images AS img
	on art.`id` = img.artist_id
WHERE
	art.genre = "인상주의"
limit 3
</pre>

---------


### 3. images table에 새로운 데이터 추가하기(query statement 만)

**답안**: 


<pre>
INSERT INTO `images` 
(
	image_url,
	title,
	year,
	artist_id,
	description
)
VALUES 
( 
	'http://cfile30.uf.tistory.com/image/1358494B4EE3321D569B49',
	'까마귀가 나는 밀밭',
	1890,
	(select id from artists
		where
	name = '빈센트 반 고흐')
	,'캔버스에 유채'
)
</pre>

images 테이블의 id는 **AUTO_INCREMENT** 속성을 갖고있기 때문에 별도로 입력하지 않아도 된다고 생각하여 입력을 생략했습니다<br>
유저는 우리가 정의한 artist_id를 모르고 이름만 알고있다고 가정했습니다.<br>
(만약 이 부분을 제가 개발된다면 예술가의 이름은 띄어쓰기를 고려하여 checkbox나 drop down을 사용하여 직접 입력받는게 아니라
개발자가 제안하는것이 효율적이라고 생각했습니다)

---------

### 4. 가장 많은 images를 갖고있는 artist 찾아오기

**답안:** 빈센트 반 고흐


<pre>
SELECT
	count(*) as image_amount, art.name
FROM
	artists as art
LEFT JOIN images AS img
	on art.`id` = img.artist_id
group by
	art.name
order by
	image_amount desc
limit 1
</pre>

최대의 갯수를 가지는 예술가가 **1명**이라고 가정한 경우의 쿼리입니다.<br>
예술가의 이름으로 group을 정하고 count로 작품의 갯수를 파악했습니다.<br>
그리고 그 갯수를 기준으로 내림차순 정렬하여 가장 높은 숫자 1개만 나오도록 만들었습니다.<br>
이 경우엔 반드시 최대값만 결과로 나오게 됩니다.


하지만 최대값이 **중복**되는 경우를 고려해야한다고 생각했습니다.


<pre>
select
	art.*, img.*
from
	artists as art
left join images as img
	on art.id = img.artist_id
left join 
	(SELECT
		count(*) as image_amount, i.artist_id as artist_id
	FROM
		artists as a
	LEFT JOIN images AS i
		on a.`id` = i.artist_id
	group by
		a.name
	) as amount
on amount.artist_id = art.id
where
	amount.image_amount = (SELECT
					count(*) as image_amount
				FROM
					artists as art
				LEFT JOIN images AS img
					on art.`id` = img.artist_id
				group by
					art.name
				order by
					image_amount desc
				limit 1
				)
group by
	img.artist_id

</pre>

테이블 artists와 images를 outer join으로 사용했지만 서브쿼리를 하나의 테이블로 간주했습니다.
이 테이블은 각 예술가가 몇 개의 작품이 있는지만 알려주는 테이블이고 가명을 amount로 정했습니다.
3개의 테이블을 left join하고 그곳에서 가장 큰 수를 찾기위해 첫 번째 쿼리를 where문에 조건검색을 위해 사용했습니다


그런데 images에서 불러오는 정보가 없고, 예술가의 이름을 **서브쿼리**에서 가져와야겠다고 생각했습니다.


<pre>
SELECT
	amount.name
FROM
	(SELECT
		count(*) as image_amount, i.artist_id as artist_id, a.name
	FROM
		artists as a
	LEFT JOIN images AS i
		on a.`id` = i.artist_id
	group by
		a.name
	) as amount

WHERE
	amount.image_amount = (SELECT
					count(*) as image_amount
				FROM
					artists as art
				LEFT JOIN images AS img
					on art.`id` = img.artist_id
				group by
					art.name
				order by
					image_amount desc
				limit 1
				)
</pre>


이 쿼리를 최종 답안으로 제출합니다.
