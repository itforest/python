1. class 클래스

    (1) 클래스 생성
        - 코드
            class BusinessCard:
                pass
    
            #pass : 내용 정의 없이 class 만들수 있음
        - 객체 생성
            card1 = BusinessCard()
  
    (2) 클래스 생성 + 함수 추가
        - 클래스 생성 + 함수 코드
          class BusinessCard:
            def set_info(self, name, email, addr):
                self.name = name
                self.email = email
                self.addr = addr
        # self : 클래스 내부에 정의된 함수의 첫번째 인자는 self 여야함!!암기!!
        - 객체 생성 및 함수 사용
            member1 = BusinessCard()
            member1.set_info("Yuna Kim", "yunakim@naver.com", "Seoul")
        - 출력
            member1.name
            'Yuna Kim'
            member1.email
            'yunakim@naver.com'
            
    (3) 클래스 생성자    
        - 생성자 코드
        class MyClass:
            def __init__(self):
                print("객체가 생성되었습니다")
        # _init__(self) 클래스의 인스턴스를 생성할때 자동으로 호출되는 메서드
        
        - 생성자를 활용한 클래스 생성 코드
        class BusinessCard:
            def __init__(self, name, email, addr):
                self.name = name
                self.email = email
                self.addr = addr
            def print_info(self):
                print("--------------------")
                print("Name : ", self.name)
                print("E-mail: ", self.email)
                print("Address: ", self.addr)
                print("--------------------")
        - 위 클래스 인스턴스 생성 코드
        member1 = BusinessCard() #__init__ 생성자의 파라미터를 입력하지 않으므로 에러!!
        member1 = BusinessCard("hokyun","hokyun@gmail.com","anyang")
        - 출력
        member1.print_info()
        --------------------
        Name : hokyun
        E-mail: hokyun@gmail.com
        Address: anyang
        --------------------
    (4) 클래스 네임스페이스
        # 네임스페이스 : 변수가 객체를 바인딩할때 그 둘 사이의 관계를 저장하고 있는 공간을 의미
        # 파이썬에서는 클래스가 정의되면 하나의 독립적인 네임스페이스가 생성되고,
        # 클래스 내의 변수나 메서드는 해당 네임스페이스 안에 딕셔너리 형태로 저장됨.
        
        - 코드 
        class Stock:
            market = "kospi"
            
        # 네임스페이스 이름 : Stock , 그리그 그 안에 변수는 딕셔너리 형태로 저장 {'Market':'kospi'} 
        
        - 클래스 네임스페이스 확인
        # 위 클래스의 네임스페임스를 확인하려면 __dict__로 확인,
           코드 : Stock.__dict__
        # 인스턴스를 생성하면 독립적으로 인스턴스의 네임스페이스를 생성함
    
    (5) 클래스 변수와 인스턴스 변수
                
                
         
        


