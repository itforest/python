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
        # self : 클래스 내부에 정의된 함수의 첫번째 인자는 반드시 self 여야함!!암기!!
        - 객체 생성 및 함수 사용
            member1 = BusinessCard()
            member1.set_info("Yuna Kim", "yunakim@naver.com", "Seoul")
        - 출력
            member1.name
            'Yuna Kim'
            member1.email
            'yunakim@naver.com'
        
        
         
        


