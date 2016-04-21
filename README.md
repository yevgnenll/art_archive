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
