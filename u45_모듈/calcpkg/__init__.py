#최초) 빈파일상관없다
#같은 폴더 안에 패키지 파일을 만든다.
#폴더안에 이 파일이 있으면 해당폴더는 패키지로인식된다
#__init__.py 파일에서 from import를 사용할 수 있다.
#__init__.py 파일에서 __all__을 사용하여 패키지에서 공개할 변수, 함수, 클래스를 지정할 수 있다.
#파이썬 3.3 이상부터는 __init__.py 파일이 없어도 패키지로 인식된다.

#두번째)
#from . import operation    # 현재. 패키지에서 operation 모듈을 가져옴
#from . import geometry     # 현재. 패키지에서 geometry 모듈을 가져옴

#세번째)main2.py
from .operation import *  
from .geometry import *    