��ġ
�Ƴ��ܴ� = ���̽� + ��Ű��

[1] ����
    - binding(���ε�) : ����Ű��
     1. ���ڿ�
         �ڵ� : MyString = 'Hello world'

     2. �ε��� , �����̽�
         �ڵ� : MyString[0:5]
         ��� : Hello

     3. ���ڿ� ������
         �ڵ� : my-jusik = "naver daum"
                   s = my-jusik.split(' ') // ['naver' , 'daum']
         naver ����ڵ� 
               ù��° ��� : my-jusik.split(' ')[0]
               �ι�° ��� : s[0]

[2] ������
     1. ������ Ÿ��
        - ���� : int(100)
        - �Ǽ� : float(3.14)
        - ���ڿ� : str("python")
    2. ������ Ȯ���ϴ� ���
        �ڵ� : type(100)
        ��� : <class 'int'>

[3] �⺻ �ڷᱸ��
     1. ����Ʈ [ ]
         1) ����Ʈ����
               �ڵ� : Mystock = ['naver',5000]
               naver ����ڵ� : Mystock[0]
         2) ����Ʈ �����̽�
                kospi_top10 = ['a','b','c','d','e','f','g','h','i','j','k']
               �ڵ� : kospi_top10[0:5]
               ��� : ['a','b','c','d','e']
         3) ����Ʈ ������ ����
             - ù��° ��� : append (�ǵڿ� ����)
               �ڵ� : kospi_top10.append('L')
               ��� :  ['a','b','c','d','e','f','g','h','i','j','k','L']
             - �ι�° ��� : insert (���ϴ� ��ġ�� ����)
               �ڵ� : kospi_top10.insert(3,'L')
               ��� :  ['a','b','c','L','d','e','f','g','h','i','j','k']
         4) ����Ʈ ������ ����
             - ����Ʈ ���� Ȯ��
                �ڵ� : len(kospi_top10)
                ��� : 11
             - ����Ʈ ������ ���� 
                �ڵ� : del kospi_top10[-1] //�ǵ� ������ ����

    2. Ʃ�� ( )
        - ����Ʈ�� Ʃ���� ������ : [ ] ��� ( ) �� ��� , Ʃ���� ������ ���� �Ұ�!! , ��� �ӵ��� ���� 

        1) Ʃ�� ����
            �ڵ� : t = ('samsung','LG', 'SK')
        2) Ʃ�� �����̽�
            �ڵ� : t[0:2] // �����̽��� [ ] ��ȣ ����Կ� ����!!

    3. ��ųʸ� { }
        - Ű, ���� ������ �̷���� ������ , { } ��ȣ ���
        1) ��ųʸ� ����
            �ڵ� : cur_price = {}
                      cur_price['daeshin'] = 30000
            ��� : {'daeshin',:30000}
        2) ��ųʸ� ������ ����
            �ڵ� : cur_price['naver'] = 80000
            ��� : {'naver',80000:'daeshin',30000}
        3) ��ųʸ� ������ ����
            �ڵ� : del cur_price['daeshin']

        4) Ű�� ���
            �ڵ� : cur_price.keys()
            ��� : dict_keys(['naver','daeshin'])    //dict_keys !!
        5) ��ųʸ�Ű,���� -> ����Ʈ�� ��ȯ
            �ڵ� : list(cur_price.keys())
            ��� : ['naver','daeshin']
            �ڵ� : list(cur_price.values())
            ��� : [80000,30000]
         6) Ű ã��
             �ڵ� : 'Samsung' in cur_price.keys()
             ��� : False
[4] �Լ�
        1) �Լ� ����
           �ڵ� : def print_ntimes(n):
                           for i in range(n):
                                      print("�������")
           ����ڵ� : print_ntimes(2)
           ��� : �������
                      �������
        2) ��ȯ���� �ִ� �Լ�
            �ڵ� : def cal_upper(price):
                             increment = price * 0.3
                             upper_price = price + increment
                             return upper_price
            ����ڵ� : cal_upper(10000)
            ��� : 13000
        3) �ΰ��� �� ��ȯ�ϱ�
             �ڵ� : def cal_upper_lower(price)
                              offset = price * 0.3
                              upper = price + offset
                              lower = price - offset
                              return ( upper, lower)
             ����ڵ� : (upper,lower) = cal_upper_lower(10000)
                     ��� :  upper
                                 13000
                                 lower
                                   7000

[5] ���
    - ��� : ���� ������ �ۼ��� ���̽� �ڵ�

 







