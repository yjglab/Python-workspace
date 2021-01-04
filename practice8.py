### 내장 함수 / "검색 list of python builtins" 에서 더 많은 정보 확인 가능

'''
# input
language = input("어떤 언어를 좋아하세요?")
print("{0}은(는) 좋은 언어입니다".format(language))
'''

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는 지 표시
print(dir())
import random # 외장 함수
print(dir())
import pickle
print(dir())

print()

print(dir(random)) # random 내장 함수에서 쓸수있는 정보들 출력

lst = [1, 2, 3]
print(dir(lst)) # lst 변수에서 쓸수있는 list 정보들 출력

print()

name = "june"
print(dir(name)) # name 변수에서 쓸 수있는 정보들 출력

print()
### 외장 함수 / "검색 list of python modules" 에서 더 많은 정보 확인 가능

#ex.
# glob : 경로 내의 폴더, 파일 목록 조회
import glob
print(glob.glob("*.py")) # .py 형식의 모든 파일에 대한 정보 출력 

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리 표시 # C:\JaeGyeong\PythonWorkspace

folder = "sample_dir"

if os.path.exists(folder): # "sample_dir"폴더가 있으면 이 구문을 들어갈 것.
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제했습니다.")
else:
    os.makedirs(folder) # "sample_dir" 폴더 생성
    print(folder, "폴더를 생성했습니다")

print()
print(os.listdir()) 

print()

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 2021-01-04 21:36:32

import datetime
print("오늘의 날짜는", datetime.date.today()) # 오늘의 날짜는 2021-01-04

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100) # 100 days를 저장
print("오늘부터 100일 이후는", today + td) # 오늘부터 100일 이후는 2021-04-14

print()

#--
import byme
byme.sign()