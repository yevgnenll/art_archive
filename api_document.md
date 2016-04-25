### 5. art_archive를 api로 설계

**우리 API는 다음 method를 사용합니다**

* **GET**: 서버에서 데이터를 찾아옵니다.
* **POST**: 서버에 데이터를 입력합니다.
* **PUT**: 서버의 데이터를 갱신합니다.
* **DELETE**: 서버의 데이터를 삭제합니다.


### art_archive의 Endpoint


| Action | HTTP method | URI |
| ------------- | ------------- | ------------- |
| 작품의 list | GET | /api/image/?page=page&count=count |
| 예술가의 list | GET | /api/artist/?page=page&count=count |
| 작품 이름 검색 list | GET | /api/image/*keyword*?page=page&count=count |
| 예술가 이름 검색 list | GET | /api/artist/*keyword*?page=page&count=count |
| 작품 상세정보 | GET | /api/image/*id* |
| 예술가 상세정보 | GET | /api/artist/*id* |
| 작품 입력 | POST | /api/image/ |
| 예술가 입력 | POST | /api/artist/ |
| 작품 수정 | PUT | /api/image/*id* |
| 예술가 수정 | PUT | /api/artist/*id* |
| 작품 삭제 | DELETE | /api/image/*id* |
| 예술가 삭제 | DELETE | /api/artist/*id* |


### art_archive의 Resources


| Resource |  URI |
| ------------- | ------------- |
| 작품의 list |  /api/image/ |
| 예술가의 list |  /api/artist/ |
| 작품 |  /api/image/*id* |
| 예술가 |  /api/artist/*id* |



#### 1. 작품 list 보여주기

* **URL**

/api/image/:keyword?page=page&count=count<br>

* **Method**

    `GET`

* **URL Param**

**required:**<br>
page=[Integer] default = 1 현재페이지
count=[Integer] default = 10 한 페이지에 보여줄 결과의 갯수

1. 검색어가 있는 경우<br>
keyword=[String] 예술가이름, 장르, 국가, 작품제목, 설명

2. 검색어가 없는 경우<br>
/api/image?page=page&count=count 까지만 입력


* **SUCCESS Response**

    * **code**: 200<br>
    **pagination**: <pre> { current_page: 1, next_url: '/api/image/page=2&count=입력받은 수'} </pre>
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

    * **code**: 404<br>
    **content**: <pre> { error: "Data doesn't exist" } </pre> 

    * **code**: 500<br>
    **content**: <pre> { error: "Internal Server Error" } </pre> 


* **Sample Code**

```
  $.ajax({
    url: "/api/image/?page=1&count=15",
    dataType: "json",
    type : "GET",
    success : function(result) {
      console.log(result);
    }
  });

  $.ajax({
    url: "/api/image/{검색어}?page=2&count=15",
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

/api/artist/:keyword?page=page&count=count<br>

* **Method**

    `GET`

* **URL Param**

**required:**<br>
page=[Integer] default is 1, 현재 페이지
count=[Integer] default is 10, 한 페이지에 보여줄 갯수

1. 검색어가 있는 경우<br>
keyword=[String] 예술가이름, 장르, 국가, 작품제목, 설명

2. 검색어가 없는 경우<br>
/api/artist?page=page&count=count 까지 입력

* **SUCCESS Response**

    * **code**: 200<br>
    **pagination**: <pre> { current_page: 1, next_url: '/api/artist?page=2&count=입력받은 수'} </pre>
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

    * **code**: 404<br>
    **content**: <pre> { error: "Data doesn't exist" } </pre> 

    * **code**: 500<br>
    **content**: <pre> { error: "Internal Server Error" } </pre> 


* **Sample Code**

```
  $.ajax({
    url: "/api/artist?page=1&count=15",
    dataType: "json",
    type : "GET",
    success : function(result) {
      console.log(result);
    }
  });

  $.ajax({
    url: "/api/artist/검색어?page=1&count=15",
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

/api/image/:id<br>

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

    * **code**: 404<br>
    **content**: <pre> { error: "Image doesn't exist" } </pre> 

    * **code**: 500<br>
    **content**: <pre> { error: "Internal Server Error" } </pre> 


* **Sample Code**

```
  $.ajax({
    url: "/api/image/100",
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

/api/artist/:id<br>

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

    * **code**: 404<br>
    **content**: <pre> { error: "Artist doesn't exist" } </pre> 

    * **code**: 500<br>
    **content**: <pre> { error: "Internal Server Error" } </pre> 


* **Sample Code**

```
  $.ajax({
    url: "/api/artist/100",
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

    /api/image/

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
    <pre> { result: "Created"} </pre>

* **ERROR Response**

    * **code**: 400<br>
    **content**: <pre> { error: "Bad Request" } </pre> 

    * **code**: 500<br>
    **content**: <pre> { error: "Internal Server Error" } </pre> 


* **Sample Code**

```
  $.ajax({
    url: "/api/image/",
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

    /api/artist/

* **Method**

    `POST`

* **URL Param**

    * **required:**<br>
        name=[String] <br>
        birth_year=[Integer] <br>
        country=[String] <br>
        genre=[String] <br>

death_year=[Integer] <br>
(살아있는 예술가에 대해서는 death_year을 입력받지 않습니다)

    * **discription**:
        birth_year, death_year는 연도만 입력합니다. <br>
        예술가의 id는 자동으로 부여됩니다.


* **SUCCESS Response**

    * **code**: 201<br>
    **content**:
    <pre> { result: "Created"} </pre>

* **ERROR Response**

    * **code**: 400<br>
    **content**: <pre> { error: "Bad Request" } </pre> 

    * **code**: 500<br>
    **content**: <pre> { error: "Internal Server Error" } </pre> 


* **Sample Code**

```
  $.ajax({
    url: "/api/artist/",
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

    * **code**: 500<br>
    **content**: <pre> { error: "Internal Server Error" } </pre> 


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

    * **code**: 500<br>
    **content**: <pre> { error: "Internal Server Error" } </pre> 


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

    * **code**: 500<br>
    **content**: <pre> { error: "Internal Server Error" } </pre> 


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

    * **code**: 500<br>
    **content**: <pre> { error: "Internal Server Error" } </pre> 


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

