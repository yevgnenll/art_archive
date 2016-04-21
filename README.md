# art_archive
tumblbug artist data project

## Junior Software Engineer Project #1
[ref](https://gist.github.com/iros/3426278) see later 

this project is deal with famouse artists and their masterpiece data

additional will be added

### 3. answer
1. 쓰레기 셀카
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
