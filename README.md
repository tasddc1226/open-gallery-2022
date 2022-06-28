## survey-management

### 프로젝트 구조
```bash
.
├── README.md
├── config
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── my_settings.py
├── requirements.txt
└── survey
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── templates
    │   ├── _base.html
    │   ├── auth
    │   │   ├── login.html
    │   │   └── signup.html
    │   ├── home.html
    │   └── survey
    │       ├── choices.html
    │       ├── create.html
    │       ├── detail.html
    │       ├── edit.html
    │       ├── list.html
    │       ├── question.html
    │       ├── search.html
    │       ├── start.html
    │       ├── submit.html
    │       └── thanks.html
    ├── tests.py
    ├── urls.py
    └── views
        ├── auth.py
        ├── home.py
        └── survey.py

6 directories, 31 files
```

<br>

### 프로젝트 목표
- 설문지 CRUD 관리자 페이지
- 특정 설문지에 대한 사용자 페이지

<br>

### 프로젝트 사용 기술
- ES6
- Django FBV
- MySQL
- black

<br>

### 요구사항 분석
- 새로운 설문지 추가
    - [x] 제목, 원하는 유형의 문항을 원하는 개수만큼 생성
    - [x] 특정 문항을 삭제할 수 있도록
    - [x] 각 문항은 제목과 두 개 이상의 선택지 작성
    - [x] 문항의 유형(type)은 Checkbox(1개 이상), Radio(1개), Select(1개) 중 하나
    
- 기존 설문지 수정
    - 새로운 설문지를 추가하는 UI/UX와 동일하게 구현
    - [x] 설문지가 비활성화 상태인 경우에만 수정할 수 있도록 구현

- 관리자 페이지
    - 설문지 목록 페이지
        - [x] 모든 설문지의 정보를 테이블 형식으로 조회
        - [x] 각 설문지의 제목, 문항 수, 응답자 수 등을 조회
            - 특정 설문지에 대한 detail 페이지에서 확인 가능
        - [x] 특정 설문지를 수정 혹은 삭제하는 버튼 구현
        - [x] 사용자에게 보낼 링크를 복사하는 버튼 구현
            - 특정 설문지에 대한 detail 페이지에서 url 확인 가능
        - [x] 삭제 버튼 클릭 시 경고(alert)와 함께 삭제 후 Refresh
        - [x] 설문지의 제목 or 설문지의 질문을 기준으로 키워드 검색 기능 + 페이지네이션 기능

    - 설문지 상세 페이지
        - [x] 각 문항의 선택지 별 응답 비율과 같은 통계 정보 조회
        - [x] (추가로) 특정 설문지의 정보를 CSV 파일로 저장할 수 있는 기능

- 사용자 페이지
    - [x] 특정 설문지를 대상으로 설문을 진행
    - [x] 각 항목에 응답 후, 전화번호를 입력한 후 제출
        - User 및 인증, 인가 불필요, admin만 사용
            - 진행하면서 설문지를 만드는 유저가 필요하다 생각되어 변경
            - 한 유저는 여러 설문지를 가질 수 있고, 해당 설문지의 링크는 인증, 권한 불필요

<br>

### DB Diagram
    
![Untitled](https://user-images.githubusercontent.com/55699007/172838655-229f41f1-0208-4de1-a4d3-7f1ebd550c6d.png)


<br>


### 유저 시나리오

<br>

#### 설문 관리자 시나리오
- 설문지를 작성하기 위해서는 회원가입을 해야한다.
- 로그인이 완료되면 설문을 생성할 수 있다.
- 생성된 설문에 대한 질문을 생성할 수 있다.
- 질문에 대한 항목들을 추가할 수 있다.
- 설문지 작성이 완료되었다면 설문지를 활성화하기 전까지는 수정을 할 수 있다.
- 설문지를 활성화 하면 해당 설문지의 링크를 알 수 있으며 각 항목에 대한 응답 비율과 참여자의 수를 알 수 있다.
- 또한 해당 설문지의 질문과 항목들을 csv 파일로 다운로드 받을 수 있다.

<br>

#### 설문 참여자 시나리오
- 설문 참여 링크를 통해서 접속한다.
- 로그인이 필요없이 해당 설문에 대한 응답을 작성한다.
- 응답을 제출한다.

<br>

### API 명세

|Method|Description|Request URL|
|:-:|:--|:--|
|GET|모든 설문지 리스트 |surveys|
|GET|특정 설문지 조회 |surveys/{survey_pk}|
|POST|설문지 생성|surveys|
|POST|설문지 질문 생성 |surveys/{survey_pk}/question|
|DELETE|설문지 질문 삭제 |surveys/{survey_pk}/question/{question_pk}/delete|
|POST|설문지 항목 생성 |surveys/{survey_pk}/question/{question_pk}/choice|
|GET|특정 설문지 시작 |surveys/{survey_pk}/start|
|POST|특정 설문지 응답 제출 |surveys/{survey_pk}/sumbit/{sub_pk}|
|POST|설문지 수정 |surveys/{survey_pk}/edit|
|DELETE|설문지 삭제 |surveys/{survey_pk}/delete|
|GET|설문지 제목 검색 |surveys/search/?q={query}|
|GET|설문지 다운로드 |surveys/{survey_pk}/download|


<br>

## Local 환경 테스트(MAC OS 기준)

#### 1. 터미널에에서 프로그램을 내려받을 폴더로 이동  (Documents 디렉터리 예시)

```bash
% cd ~/Documents
```

#### 2. git clone으로 파일을 받고 프로젝트 폴더로 이동 

```bash
% git clone https://github.com/tasddc1226/open-gallery-2022.git
% cd open-gallery-2022
```



#### 3. 폴더 트리 확인

```bash
% ls

# 예시 화면
README.md        __pycache__      config           manage.py        my_settings.py   requirements.txt survey           venv
```


#### 4. 파이썬 설치 확인

```bash
% python --version

# 예시화면
Python 3.8.10
```

#### 5. 가상환경 생성

```bash
% python -m venv venv
```



#### 6. 가상환경 진입

```bash
% source venv/bin/activate
```



#### 7. 파이썬 모듈 설치

```bash
% pip install --upgrade pip
% pip install -r requirements.txt
```

#### 8. 환경변수 파일 만들기

###### 프로젝트 폴더에서 파일명 my_settings.py를 만들고 아래의 내용을 붙여넣기

```python
# my_settings.py

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'open',
        'USER': 'root',
        'PASSWORD': 'mysecretpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    'OPTIONS': {'charset': 'utf8mb4'}
    }
}

SECRET_KEY = 'thisismysecretkey'
DEBUG = True
```



#### 9. 로컬 환경에 Mysql 설치

###### 이미 Mysql이 설치되어있다면 이 과정은 넘어가도 된다. 만약 brew가 설치되어 있지 않다면 [이곳](https://brew.sh/index_ko)을 참고 

```bash
% brew install mysql
% brew services start mysql
```

###### 루트 비밀번호 세팅 (이곳 비밀번호가 8번 환경변수 파일 만들기의 비밀번호에 들어가야한다.)

```bash
% mysqladmin -u root password 'mysecretpassword'
```

###### 터미널에서 mysql 접속확인

```bash
% mysql -u root -p
% mysecretpassword
```

#### 10. database 생성

###### mysql에 접속하였다면 터미널 명령창이 아래와 같이 mysql> 로 바뀐다.

```mysql
mysql> create database open character set utf8mb4 collate utf8mb4_general_ci;
```

#### 11. Django를 이용한 Mysql DB 테이블 생성

###### 프로젝트 폴더(3번 참고)로 이동하여 아래와 같이 입력

```bash
% python manage.py migrate
```

#### 12. Django 서버 실행

###### 프로젝트 폴더에서 아래의 명령어를 입력

```bash
% python manage.py runserver
```

---
