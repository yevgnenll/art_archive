# art_archive
tumblbug artist data project

## Junior Software Engineer Project #1
[ref](https://gist.github.com/iros/3426278) see later 

this project is deal with famous artists and their masterpiece data

additional will be added

## 3. 다음 작업을 수행하는 SQL query들과 해당 리턴값을 작성해주시기 바랍니다.
 

[답안](./query.md)


---------

### 4. CRUD에 대한 설명

CRUD는 Create(생성), Read(읽기), Update(수정), Delete(삭제) 를 말합니다.
이 CRUD를 API와 sql query 관점에서 데이터를 송신할때 method(http request)와 query는 아래와 같습니다


| CRUD | method | sql query |
| ------------- | ------------- | ------------- |
| Create | POST  | INSERT |
| Read  | GET  | SELECT |
| Update  | PUT  | UPDATE |
| Delete  | DELETE  | DELETE |


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
        "title": "작품제목",
        "artist_id": 예술가의 id,
        "image_url": "이미지 링크",
        "year": "작품이 만들어진 연도",
        "description": "작품 설명"
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
        "title": "예술가의 이름",
        "birth_year": "출생연도",
        "death_year": "사망연도",
        "country": "예술가의 국가"
        "genre": "예술가의 장르"
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

    /api/image/:id

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

    * **code**: 400<br>
    **content**: <pre> { error: "Bad Request" } </pre> 

    * **code**: 404<br>
    **content**: <pre> { error: "Not Found" } </pre> 


* **Sample Code**

```
  $.ajax({
    url: "/api/image/{id}",
    dataType: "json",
    type : "PUT",
    data : {
        "title": "작품 제목",
        "image_url": "작품 이미지 url",
        "year": "작품이 만들어진 연도",
        "description": "작품설명"
        }
    success : function(result) {
      console.log(result);
    }
  });

```

------


#### 8. 예술가 정보 수정하기 

기존에 입력된 예술가의 정보를 수정합니다.<br>
입력되지 않은 정보들에 대해서는 수정을 반영하지 않습니다.<br>
데이터의 신뢰성을 보장하기 위해 공백 수정은 반려합니다.


* **URL**

    /api/artist/:id

* **Method**

    `PUT`

* **URL Param**

    * **required:**<br>
        id=[Integer]

    name=[String] <br>
    birth_year=[Integer] <br>
    death_year=[Integer] <br>
    country=[String] <br>
    genre=[String] <br>


* **SUCCESS Response**

    * **code**: 200<br>
    **content**:
    <pre> { result: "OK"} </pre>

* **ERROR Response**

    * **code**: 400<br>
    **content**: <pre> { error: "Bad Request" } </pre> 

    * **code**: 404<br>
    **content**: <pre> { error: "Not Found" } </pre> 


* **Sample Code**

```
  $.ajax({
    url: "/api/artist/{id}",
    dataType: "json",
    type : "PUT",
    data : {
        "name": "예술가의 이름",
        "birth_year": "출생연도",
        "death_year": "사망연도",
        "country": "예술가의 국가",
        "genre": "예술가의 장르"
        }
    success : function(result) {
      console.log(result);
    }
  });

```

------

#### 9. 작품정보 삭제하기


* **URL**

    /api/image/:id

* **Method**

    `DELETE`

* **URL Param**

    * **required:**<br>
        id=[Integer]

* **SUCCESS Response**

    * **code**: 204<br>
    **content**:
    <pre> { result: "No Content"} </pre>

* **ERROR Response**

    * **code**: 404<br>
    **content**: <pre> { error: "Not Found" } </pre> 


* **Sample Code**

```
  $.ajax({
    url: "/api/image/{id}",
    dataType: "json",
    type : "DELETE",
    success : function(result) {
      console.log(result);
    }
  });

```

------

#### 10. 예술가 정보 삭제하기

예술가 정보를 삭제는 주의가 필요합니다.
해당 예술가로 등록되어있는 모든 작품 정보가 함께 삭제됩니다


* **URL**

    /api/artist/:id

* **Method**

    `DELETE`

* **URL Param**

    * **required:**<br>
        id=[Integer]


* **SUCCESS Response**

    * **code**: 204<br>
    **content**:
    <pre> { result: "No Content"} </pre>

* **ERROR Response**

    * **code**: 404<br>
    **content**: <pre> { error: "Not Found" } </pre> 


* **Sample Code**

```
  $.ajax({
    url: "/api/artist/{id}",
    dataType: "json",
    type : "DELETE",
    success : function(result) {
      console.log(result);
    }
  });

```

------

