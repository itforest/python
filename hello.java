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
     1. 리스트
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


