# if 사용법
# if는 정말 많이쓰인다f
A = 3
B = 2

if A == B :
    print('Ture')     #만약 A와 B가 같다면 Ture를 출력한다 
                      #if 문을 사용한 후에 뒤에는 꼭 " : " 을 붙이고 if문의 조건을 만족했을때 나오는 이벤트는 if문 아랫줄에서 4번 띄어씀
if A == B :
    A = 3
    B = 3
    print(A)     #단순한 예 A 가 3이고 B가 2이기 때문에 조건이 성림되지않아 작동하지 않는다
if not A == B:
    A == 3
    B == 3
    print(A)     #if 뒤에 not을 붙여서 조건이 성립되지 않으면 이벤트가 발생하게 한다
    
    
    
    
    #2.   부등식
    
    A == B # A는 B와 같다
    A < B # A는 B보다 작다
    A =< B # A는B보다 작거나 같다
    A != B # A는 B와 같지 않다