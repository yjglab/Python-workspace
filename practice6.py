### 패키지 : 불러오기

import travelPackage.thailand # import package파일.뒤에는 반드시 모듈 파일 혹은 패키지 파일만 올 수 있음
tripTo = travelPackage.thailand.ThailandPackage()
tripTo.detail() # [태국 패키지] 방콕, 파타야 투어

from travelPackage.thailand import ThailandPackage # from - import 문에서는 클래스도 가져올 수 있음
tripTo = ThailandPackage()
tripTo.detail() # [태국 패키지] 방콕, 파타야 투어

from travelPackage import vietnam
tripTo = vietnam.VietnamPackage()
tripTo.detail() # [베트남 패키지] 다낭 투어

### __all__
from travelPackage import * # 패키지 파일(폴더)의 __init__.py 에서 공개범위를 설정.
tripTo = vietnam.VietnamPackage()
tripTo.detail() # [베트남 패키지] 다낭 투어
tripTo = thailand.ThailandPackage()
tripTo.detail() # [태국 패키지] 방콕, 파타야 투어


### 패키지, 모듈의 위치 알아내기 
from travelPackage import *
import inspect
import random
print(inspect.getfile(random)) # C:\Python39\lib\random.py
print(inspect.getfile(thailand)) # c:\JaeGyeong\PythonWorkspace\travelPackage\thailand.py

