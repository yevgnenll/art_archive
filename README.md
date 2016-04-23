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

### 5. art_archive를 api로 설계, document 만들기

[답안](./api_document.md)


#### 고려할 사항

- API Resource
- 어떤 endpoint를 갖는지
- endpoint 별로 받는 param
- 성공과 실패시 response

--------
### 6. TDD 를 설명해주세요. 이 개발 방식의 장단점은 무엇일까요? 

* **TDD란?**: Test Driven Development 테스트 주도 개발


개발을 시작하면 엔지니어가 개발을 구현하는 기능을 먼저 만드는것이 아니라<br>
테스트 코드를 먼저 만들어(처음엔 무조건 실패하는 테스트코드) 그 테스트를 통과하는<br>
코드를 만들고, 후에 엔지니어의 프로젝트에 알맞도록 리팩토링 한다.


장점: 정의에서 표현되었듯 리팩토링 하기에 편하다.<br>
저는 리팩토링을 좋아하는데, 이유는 군살없는 논리적인 코드가 나왔을때 말로 표현못할 뿌듯함을 느낍니다.<br>
하지만 아직까진 처음 작성한 코드가 이렇게 되기란 쉽지 않습니다.<br>
테스트코드가 있고, 그 결과가 정확하다면 저는 테스트코드를 믿고 리팩토링을 하는데 어려움이 없을것입니다.<br>


예전에 TDD를 몰랐을때 유저 등록폼을 만들었는데 그 폼 하나에서 발생되는 경우의 수가 약 20가지였습니다.<br>
그때 20가지를 모두 테스트 하는게 두려웠는데 TDD를 적용한다면<br>
두려움 없이 리팩토링을 할 것이고 다양한 시도를 해볼 수 있습니다.<br>


단점: 테스트 코드를 짜는것이 생산성에 영향을 준다<br>
먼저 테스트 코드를 학습해야 하고, 이것을 내 프로젝트에 알맞게 적용해야 합니다.<br>
패스트캠퍼스의 hiring day를 위한 프로젝트를 약 8일간 진행했는데 이때에 짧은 기간때문에<br>
테스트 코드는 이후로 미뤄야겠다는 결정을 내린 경험이 있습니다.


하지만 저는 TDD에 대해 찬성하며 테스트 코드를 만드는 시간이나 고민하며 테스트하는 시간이
비슷하리라 생각합니다.


---------

#### 소감

1번째 프로젝트를 진행하기 전에 가장 먼저 텀블벅의 core value를 다시 읽었습니다.<br>
특히 communication 부분은 테스트 과정에서 가장 크게 경험할 수 있는 텀블벅의 문화라고 생각했기 때문입니다.<br>
앞으로도 많은 커뮤니케이션이 있길 바랍니다.<br>


query 부분<br>
단순히 문제를 푸는것이 아니라 실제 서비스에서 이 부분을 구현한다면 어떻게해야할까? 를 고려했습니다.<br>
그래서 작품이 가장 많은 예술가를 찾을때를 많이 고민하고 가장 많은 시간을 투자하였습니다.<br>


api 부분<br>
내가 이것을 참고해서 개발을 한다면 어떤 정보가 필요할까? 를 염두해두고 만들었습니다.<br>
좀 더 쉽게 설명하고 싶었고 완성된 문장으로 간결하게 표현하고 싶었습니다.<br>
