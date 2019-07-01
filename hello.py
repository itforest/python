설치
아나콘다 = 파이썬 + 패키지

[1] 변수
    - binding(바인딩) : 가리키다
     1. 문자열
         코드 : MyString = 'Hello world'

     2. 인덱싱 , 슬라이싱
         코드 : MyString[0:5]
         출력 : Hello

     3. 문자열 가르기
         코드 : my-jusik = "naver daum"
                   s = my-jusik.split(' ') // ['naver' , 'daum']
         naver 출력코드 
               첫번째 방법 : my-jusik.split(' ')[0]
               두번째 방법 : s[0]

[2] 데이터
     1. 데이터 타입
        - 정수 : int(100)
        - 실수 : float(3.14)
        - 문자열 : str("python")
    2. 데이터 확인하는 방법
        코드 : type(100)
        출력 : <class 'int'>

[3] 기본 자료구조
     1. 리스트 [ ]
         1) 리스트생성
               코드 : Mystock = ['naver',5000]
               naver 출력코드 : Mystock[0]
         2) 리스트 슬라이싱
                kospi_top10 = ['a','b','c','d','e','f','g','h','i','j','k']
               코드 : kospi_top10[0:5]
               출력 : ['a','b','c','d','e']
         3) 리스트 데이터 삽입
             - 첫번째 방법 : append (맨뒤에 삽입)
               코드 : kospi_top10.append('L')
               출력 :  ['a','b','c','d','e','f','g','h','i','j','k','L']
             - 두번째 방법 : insert (원하는 위치에 삽입)
               코드 : kospi_top10.insert(3,'L')
               출력 :  ['a','b','c','L','d','e','f','g','h','i','j','k']
         4) 리스트 데이터 삭제
             - 리스트 개수 확인
                코드 : len(kospi_top10)
                출력 : 11
             - 리스트 데이터 삭제 
                코드 : del kospi_top10[-1] //맨뒤 데이터 삭제

    2. 튜플 ( )
        - 리스트와 튜플의 차이점 : [ ] 대신 ( ) 를 사용 , 튜플은 데이터 수정 불가!! , 대신 속도가 빠름 

        1) 튜플 생성
            코드 : t = ('samsung','LG', 'SK')
        2) 튜플 슬라이싱
            코드 : t[0:2] // 슬라이싱은 [ ] 기호 사용함에 주의!!

    3. 딕셔너리 { }
        - 키, 벨류 쌍으로 이루어진 데이터 , { } 기호 사용
        1) 딕셔너리 생성
            코드 : cur_price = {}
                      cur_price['daeshin'] = 30000
            출력 : {'daeshin',:30000}
        2) 딕셔너리 데이터 삽입
            코드 : cur_price['naver'] = 80000
            출력 : {'naver',80000:'daeshin',30000}
        3) 딕셔너리 데이터 삭제
            코드 : del cur_price['daeshin']

        4) 키값 출력
            코드 : cur_price.keys()
            출력 : dict_keys(['naver','daeshin'])    //dict_keys !!
        5) 딕셔너리키,벨류 -> 리스트로 변환
            코드 : list(cur_price.keys())
            출력 : ['naver','daeshin']
            코드 : list(cur_price.values())
            출력 : [80000,30000]
         6) 키 찾기
             코드 : 'Samsung' in cur_price.keys()
             출력 : False
[4] 함수
        1) 함수 생성
           코드 : def print_ntimes(n):
                           for i in range(n):
                                      print("대신증권")
           출력코드 : print_ntimes(2)
           출력 : 대신증권
                      대신증권
        2) 반환값이 있는 함수
            코드 : def cal_upper(price):
                             increment = price * 0.3
                             upper_price = price + increment
                             return upper_price
            출력코드 : cal_upper(10000)
            출력 : 13000
        3) 두개의 값 반환하기
             코드 : def cal_upper_lower(price)
                              offset = price * 0.3
                              upper = price + offset
                              lower = price - offset
                              return ( upper, lower)
             출력코드 : (upper,lower) = cal_upper_lower(10000)
                     출력 :  upper
                                 13000
                                 lower
                                   7000

[5] 모듈
    - 모듈 : 파일 단위로 작성된 파이썬 코드

 







