# art_archive
tumblbug artist data project

## Junior Software Engineer Project #1
[ref](https://gist.github.com/iros/3426278) see later 

this project is deal with famouse artists and their masterpiece data

additional will be added

### 3. answer
#### 1. 쓰레기 셀카

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

이 쿼리로 처음 확인을 하였고 refactoring은 아래와 같습니다.

at first i searched for checking and refactored below

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
작품 제목만 찾는 쿼리입니다.

search only masterpiece title

####2. 3개의 이미지

http://www.gulbenkian.pt/prjdir/gulbenkian/images/mediaRep/museu/colecao/pintura/Inv._2361Trat.jpg
http://www.manet.org/images/gallery/the-luncheon-on-the-grass.jpg
http://mfas3.s3.amazonaws.com/objects/SC232880.jpg

1번의 정답과 같이 처음엔 모든 데이터를 확인하기 위해 아래와 같이 만들었습니다

i made below sql to check all of data such as problem no.1 at first

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

results are 7 artists and 12 masterpieces but there isn't another criteria in problem 
so i wrote like below

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

#### 3. images table에 새로운 데이터 추가하기

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

images 테이블의 id는 AUTO_INCREMENT 속성을 갖고있기 때문에 별도로 입력하지 않아도 된다고 생각했습니다.<br>
유저는 저희가 정의한 artist_id를 모르고 이름만 알고있다고 가정했습니다.<br>
(만약 이 부분을 제가 개발된다면 예술가의 이름은 띄어쓰기를 고려하여 checkbox나 drop down을 사용하여 직접 입력받는게 아니라
개발자가 제안하는것이 유저를 배려한다고 생각합니다.)

images table attribute 'ID' has AUTO_INCREMENT so i think it isn't needed.<br>
i assume that all user doesn't know what we defined artists' id (artist_id attribute)<br>
because of word spacing i think if i develop this part i will use checkbox or dropdown <br>
not be input artist name directly. developer should propose aritsts' name for user friendly

#### 4. 가장 많은 images를 갖고있는 artist 찾아오기
(답안: 빈센트 반 고흐)

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

최대의 갯수를 가지는 예술가가 1명이라고 가정한 경우의 쿼리입니다.<br>
예술가의 이름으로 group을 정하고 count로 작품의 갯수를 파악했습니다.<br>
그리고 그 갯수를 기준으로 내림차순 정렬하여 가장 높은 숫자 1개만 나오도록 만들었습니다.<br>
이 경우엔 반드시 최대값만 결과로 나오게 됩니다.

하지만 최대값이 중복되는 경우를 고려해야한다고 생각했습니다.

this query is max image count is only one, at first<br>
group by artists' name and i got each artists' amount of masterpieces using count() function<br>
and i got max in descanding order base on each its the number of amount <br>
in this case max amount must be displayed

but i think we have to consider maximun can be duplicated

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

테이블을 artists, images를 outer join으로 사용했지만 서브쿼리를 하나의 테이블로 간주했습니다.
이 테이블은 각 예술가가 몇 개의 작품이 있는지만 알려주는 테이블이고 가명을 amount로 정했습니다.
3개의 테이블을 left join하고 그곳에서 가장 큰 수를 찾기위해 첫 번째 쿼리를 where문에 조건검색을 위해 사용했습니다

그런데 images에서 불러오는 정보가 없고, 예술가의 이름을 서브쿼리에서 가져와야겠다고 생각했습니다.

i used table 'artists', 'images' with outer join but i took subquery as a table
this table let us know each artists' amount of materpiece and its alias is 'amount'
after left joining 3 tables, i used first query in 'where' to find the largest number 

but i'm not loading any information in images table, and artists' name can be found in subquery

<pre>
select 
	amount.name
from
	(SELECT
		count(*) as image_amount, i.artist_id as artist_id, a.name
	FROM
		artists as a
	LEFT JOIN images AS i
		on a.`id` = i.artist_id
	group by
		a.name
	) as amount

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
</pre>

이 쿼리를 최종 답안으로 제출합니다.

now i submit this query as a final answer
