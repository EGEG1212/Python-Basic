# 함수 2개를 갖고있는 calc.py
def add(a, b):
    return a + b
 
def mul(a, b):
    return a * b
 
 # 프로그램의 시작점일 때'나로부터 시작할때'만 아래 코드 실행
if __name__ == '__main__':    
    print(add(10, 20))
    print(mul(10, 20))