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

[답안](./api_document.md)


#### 고려할 사항

- API Resource
- 어떤 endpoint를 갖는지
- endpoint 별로 받는 param
- 성공과 실패시 response

--------

