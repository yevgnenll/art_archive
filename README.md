# art_archive
tumblbug artist data project

## Junior Software Engineer Project #1
[ref](https://gist.github.com/iros/3426278) see later 

this project is deal with famous artists and their masterpiece data

additional will be added

### 3. answer

테이블 분석: artists

| column name | attribute |
| ------------- | ------------- |
| id  | not null && auto increment  |
| name  | artist name |
| birth_year  |  artists' birth year  |
| year  | created year  |
| artist_id  | artists' id as Integer  |
| description  | explain of masterpiece  |


테이블 분석: images foreign key is artists_id from table artists

| column name | attribute |
| ------------- | ------------- |
| id  | not null && auto increment  |
| image_url  | 이미지 링크  |
| title  | 작품제목  |
| year  | 작품 생성된 연도  |
| artist_id  | artists테이블의 FK  |
| description  | 작품 특성(유채 etc.)  |

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
작품 제목만 찾는 쿼리입니다.

this query is finding title of masterpiece

####2. 3개의 이미지

answer:

http://www.gulbenkian.pt/prjdir/gulbenkian/images/mediaRep/museu/colecao/pintura/Inv._2361Trat.jpg
http://www.manet.org/images/gallery/the-luncheon-on-the-grass.jpg
http://mfas3.s3.amazonaws.com/objects/SC232880.jpg

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

---------
### 4. CRUD에 대한 설명

CRUD는 Create(생성), Read(읽기), Update(수정), Delete(삭제) 를 말합니다.
이 CRUD를 API와 sql query 관점에서 데이터를 송신할때 method(http request)와 query는 아래와 같습니다


| CRUD 종류  | method | sql query |
| ------------- | ------------- | ------------- |
| Create | POST  | INSERT |
| Read  | GET  | SELECT |
| Update  | PUT  | UPDATE |
| Delete  | DELETE  | DELETE |


위의 4가지 기능을 모두 할 수 없다면 그 소프트웨어는 완성된게 아니라는 평가를 받는다고 합니다.
가장 보편적인 예시로는 게시판의 기능을 생각할 수 있습니다.(글 쓰기, 읽기, 수정, 삭제)

--------

### 5. art_archive를 api로 설계

#### 고려할 사항

- API Resource
- 어떤 endpoint를 갖는지
- endpoint 별로 받는 param
- 성공과 실패시 response

--------

**우리 API는 다음 method를 사용합니다**

* **GET**: 서버에서 데이터를 찾아옵니다.
* **POST**: 서버에 데이터를 입력합니다.
* **PUT**: 서버의 데이터를 갱신합니다.
* **DELETE**: 서버의 데이터를 삭제합니다.


#### 1. 작품 list 보여주기

* **URL**

/api/image/list/:masterpiece/:page<br>
한 페이지에 보여주는 작품의 수는 **10개**

* **Method**

    `GET`

* **URL Param**

**required:**<br>
page=[Integer] default is 1

1. 검색어가 있는 경우<br>
masterpiece=[String] 작품제목

2. 검색어가 없는 경우<br>
masterpiece="masterpiece" 



* **SUCCESS Response**

    * **code**: 200<br>
    **pagination**: <pre> { current_page: 1, next_url: '/api/image/list/masterpiece/2'} </pre>
    **pagination**: 현재 페이지는 존재하지만 다음 페이지가 없는경우 
                    <pre> { current_page: 1, next_url: null } </pre>
    **content**: 1페이지에 10개 이하의 데이터 전송
    <pre>   { 
            id: 작품의 ID[Integer], 
            title: 작품의 제목[String] ,
            year: 작품이 만들어진 연도[Date],
            description: 작품의 설명[String],
            name: 작가 이름[String],
            genre: 작가의 장르[String],
            image_url: 작품 이미지[URL],
            }
    </pre>

* **ERROR Response**

    * **code**: 404
    **content**: <pre> { error: "Data doesn't exist" } </pre> 

* **Sample Code**

```
  $.ajax({
    url: "/api/image/list/masterpiece/1",
    dataType: "json",
    type : "GET",
    success : function(result) {
      console.log(result);
    }
  });

  $.ajax({
    url: "/api/image/list/검색어/1",
    dataType: "json",
    type : "GET",
    success : function(result) {
      console.log(result);
    }
  });

```

--------

#### 2. 예술가 list 보여주기

* **URL**

/api/artist/list/:name/:page<br>
한 페이지에 보여주는 작품의 수는 **10개**

* **Method**

    `GET`

* **URL Param**

**required:**<br>
page=[Integer]

1. 검색어가 있는 경우<br>
name=[String] artist의 이름

2. 검색어가 없는 경우<br>
name="name"


* **SUCCESS Response**

    * **code**: 200<br>
    **pagination**: <pre> { current_page: 1, next_url: '/api/artist/list/name/2'} </pre>
    **pagination**: 현재 페이지는 존재하지만 다음 페이지가 없는경우 
                    <pre> { current_page: 1, next_url: null } </pre>
    **content**: 1페이지에 10개 이하의 데이터 전송
    <pre>   { 
            id: 예술가의 ID[Integer], 
            name: 예술가의 이름[String] ,
            birth_year: 예술가의 태어난 연도[Date],
            death_year: 예술가의 사망한 연도[Date],
            genre: 예술가의 장르[String],
            }
    </pre>

* **ERROR Response**

    * **code**: 404
    **content**: <pre> { error: "Data doesn't exist" } </pre> 

* **Sample Code**

```
  $.ajax({
    url: "/api/artist/list/name/1",
    dataType: "json",
    type : "GET",
    success : function(result) {
      console.log(result);
    }
  });

  $.ajax({
    url: "/api/artist/list/검색어/1",
    dataType: "json",
    type : "GET",
    success : function(result) {
      console.log(result);
    }
  });

```

----------

#### 3. 작품 한개씩 보기(detail)

* **URL**

/api/image/detail/:id<br>

* **Method**

    `GET`

* **URL Param**

**required:**<br>
id=[Integer]


* **SUCCESS Response**

    * **code**: 200<br>
    **content**: 
    <pre>   { 
            id: 작품의 id[Integer]
            title: 작품의 제목[String] ,
            year: 작품이 만들어진 연도[Date],
            description: 작품의 설명[String],
            name: 작가 이름[String],
            genre: 작가의 장르[String],
            image_url: 작품 이미지[URL],
            }
    </pre>

* **ERROR Response**

    * **code**: 404
    **content**: <pre> { error: "Data doesn't exist" } </pre> 

* **Sample Code**

```
  $.ajax({
    url: "/api/image/detail/100",
    dataType: "json",
    type : "GET",
    success : function(result) {
      console.log(result);
    }
  });

```

----------
#### 4. 예술가 한명씩 보기(detail)

* **URL**

/api/artist/detail/:id<br>

* **Method**

    `GET`

* **URL Param**

**required:**<br>
id=[Integer]


* **SUCCESS Response**

    * **code**: 200<br>
    **content**:
    <pre>   { 
            id: 예술가의 ID[Integer],
            name: 예술가의 이름[String] ,
            birth_year: 예술가가 태어난 연도[Date],
            death_year: 예술가의 사망 연도[Date],
            contry: 예술가의 국가[String],
            genre: 예술가의 장르[String],
            }
    </pre>

* **ERROR Response**

    * **code**: 404
    **content**: <pre> { error: "Data doesn't exist" } </pre> 

* **Sample Code**

```
  $.ajax({
    url: "/api/artist/detail/100",
    dataType: "json",
    type : "GET",
    success : function(result) {
      console.log(result);
    }
  });

```

---------

#### 5. 작품 입력하기 api

작품 하나의 정보를 입력합니다. 기존에 저희 서버에 존재하는 작가의 작품을 입력하려면<br>
작가의 artist_id를 알아야 합니다. 이것은 4번 api를 참고하시기 바랍니다.


* **URL**

    /api/image/insert/

* **Method**

    `POST`

* **URL Param**

    * **required:**<br>
    artist_id=[Integer] <br>
    title=[String] <br>
    image_url=[URL] <br>
    year=[Integer] <br>
    description=[String]


    * **discription**:
        artist_id로 예술가 정보가 연결됩니다. <br>
        입력하시는 작품의 예술가 정보가 입력되어 있지 않다면 <br>
        아래의 예술가 입력 api를 이용해 함께 입력해주시기 바랍니다 <br>
        작품에 대한 고유 ID는 자동으로 부여됩니다


* **SUCCESS Response**

    * **code**: 201<br>
    **content**:
    <pre> { result: "OK"} </pre>

* **ERROR Response**

    * **code**: 400
    **content**: <pre> { error: "Bad Request" } </pre> 

* **Sample Code**

```
  $.ajax({
    url: "/api/image/insert",
    dataType: "json",
    type : "POST",
    data : {
        title: "작품제목",
        artist_id: 예술가의 id,
        image_url: "이미지 링크",
        year: "작품이 만들어진 연도",
        description: "작품 설명"
        }
    success : function(result) {
      console.log(result);
    }
  });

```

----------

#### 6. 예술가 입력하기 api

예술가 한명의 이름, 출생연도, 사망연도, 국가와 장르 정보를 입력합니다

* **URL**

    /api/artist/insert/

* **Method**

    `POST`

* **URL Param**

    * **required:**<br>
        name=[String] <br>
        birth_year=[Integer] <br>
        death_year=[Integer] <br>
        country=[String] <br>
        genre=[String] <br>


    * **discription**:
        birth_year, death_year는 연도만 입력합니다. <br>
        예술가의 id는 자동으로 부여됩니다.


* **SUCCESS Response**

    * **code**: 201<br>
    **content**:
    <pre> { result: "Created"} </pre>

* **ERROR Response**

    * **code**: 400
    **content**: <pre> { error: "Bad Request" } </pre> 

* **Sample Code**

```
  $.ajax({
    url: "/api/artist/insert",
    dataType: "json",
    type : "POST",
    data : {
        title: "예술가의 이름",
        birth_year: "출생연도",
        death_year: "사망연도",
        country: "예술가의 국가"
        genre: "예술가의 장르"
        }
    success : function(result) {
      console.log(result);
    }
  });

```

------

#### 7. 작품정보 수정하기 

기존에 입력 작품 정보를 수정할 수 있습니다.
입력되지 않은 항목에 대해서는 수정을 하지 않으며, 공백으로 수정을 원하실경우
빈칸(space)를 입력해주시면 반영됩니다.


* **URL**

    /api/artist/:id

* **Method**

    `PUT`

* **URL Param**

    * **required:**<br>
        id=[Integer]

    artist_id=[Integer] <br>
    title=[String] <br>
    image_url=[URL] <br>
    year=[Integer] <br>
    description=[String]


* **SUCCESS Response**

    * **code**: 200<br>
    **content**:
    <pre> { result: "OK"} </pre>

* **ERROR Response**

    * **code**: 400
    **content**: <pre> { error: "Bad Request" } </pre> 

    * **code**: 404
    **content**: <pre> { error: "Not Found" } </pre> 


* **Sample Code**

```
  $.ajax({
    url: "/api/artist/{id}",
    dataType: "json",
    type : "PUT",
    data : {
        title: "예술가의 이름",
        birth_year: "출생연도",
        death_year: "사망연도",
        country: "예술가의 국가"
        genre: "예술가의 장르"
        }
    success : function(result) {
      console.log(result);
    }
  });

```

------


