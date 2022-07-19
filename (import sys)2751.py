import sys
num = int(input())
m = []

for _ in range(num):
    m.append((int(sys.stdin.readline())))

m.sort()

for i in m:
    print(i)
    
    
#input() 함수는 앞에 문자열을 출력하고 입력을 받을 수 있는 기능이 있고
#문자 입력시 개행 문자를 자동으로 삭제해준다.
#따라서 많은 반복문을 통해 입력을 받을 때에는 처리 속도가 느려지는 단점이 있다.
#import sys / sys.stdin.readline()은 정말 문자만 입력받는 기능을 하고, c언어의 scanf와 같이 개행문자 자동삭제가 안된다. 따라서 입력 외에 다른 연산 기능이 없어서 수행 능력이 보다 빠르다
