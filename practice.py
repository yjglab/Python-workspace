print(not True) # False
print(not (5 < 10)) #False

# 변수
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집" + animal + "의 이름은 " + name + "에요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요") # +를 통해 정수형을 출력 시 str()을 써서 문자형으로 바꿔야함
print(name + "는 어른일까요? " + str(is_adult)) # +를 통해서는 불린형도 str()으로 바꿔야 함

print(name, "는", age, "살이며", hobby, "을 아주 좋아해요") # ,를 사용하면 다른 자료형에 str()빼도 출력 가능
# 단, 빈칸이 반드시 들어가게 됨. (ex. 연탄이 는)

# 주석 : #를 사용하거나 ''' 내용 ''' 을 사용.

# 연산자
print(5//3) # 몫 1
print(4 == 4) # True
print(1 + 3 == 4) # True
print(1 != 3) # True

print((3 > 0) and (3 < 5)) # 좌우 모두 참이여야 True 출력.
print((3 > 0) & (3 < 5)) # 위와 동일.

print((3 > 0) or (3 > 5)) # 좌우 중 하나가 참이면 True 출력.
print((3 > 0) | (3 > 5)) # 위와 동일.

print(5 > 4 > 3) # True

# 숫자 처리 함수
print(abs(-5)) # 절댓값 5
print(pow(4, 2)) # 4^2
print(max(5, 12)) # 5와 12 중 최댓값 (12)
print(min(5, 12)) # 5
print(round(3.14)) # 반올림, 3
print(round(4.99)) # 5
print(round(328/3, 2)) # 소수점 둘째 자리까지 표시, # 109.33

# math 함수
from math import * # math 내장 라이브러리를 이용하겠다.
print(floor(4.99)) #내림, 4
print(ceil(3.14)) #올림, 4
print(sqrt(16)) #제곱근, 4

# 랜덤 함수
from random import *
print(random()) # 0.0 ~ 1.0미만 사이의 난수 출력
print(random() * 10) # 0.0 ~ 10.0미만
print(int(random() * 10)) # 0 ~ 10미만 사이 정수형 난수 출력
print(int(random() * 45) + 1) # 1 ~ 45이하 사이 정수형 난수 출력

print(randrange(1, 45)) # 1 ~ 45 미만 난수 출력
print(randint(1, 45)) # 1 ~ 45 이하 난수 출력

studyDay = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 "+str(studyDay)+"일로 선정")

# 문자열
sentence = "나는 소년이다"
print(sentence)
sentence2 = """
나는 소년이며,
파이썬을 배운다
"""
print(sentence2) # 총 4줄 출력

# 슬라이싱
jumin = "961118-1426314"

print("성별 : " + jumin[7]) # 1
print("연도 : " + jumin[0:2]) # 96 (0부터 2직전까지)
print("생일 : " + jumin[:6]) # 961118 (처음부터 6직전까지)
print("뒷번 : " + jumin[7:]) # 1426314 (7부터 끝까지)
print("뒷번 : " + jumin[-7:]) # 1426314

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # "python is amazing"
print(python[0].isupper()) # True (0번 index가 대문자인가?)
print(len(python)) # 17 (문자열 길이)
print(python.replace("Python", "JavaScript")) # JavaScript is Amazing

index = python.index("n") # "n"이 위치한 index
print(index) # 5 (첫번째 n)
index = python.index("n", index + 1) # 기존 index 값에 +1을 한 index부터 "n"이 발견된 index.
print(index) # 15 (두번째 n)

print(python.find("Java")) # -1 (실제로 Java라는 값은 존재하지 않지만 오류를 출력하지 않음. python.index() 는 오류를 표시함.
                           # 오류를 표시하는 경우는 다음 코드를 출력하지 않지만 find()는 그렇지 않음.

print(python.count("n")) # 2 ("n"이 총 몇개 있는가?)

# 문자열 포맷
print("나는 %d살입니다" % 20) # 나는 20살입니다 (정수형)
print("나는 %s을 좋아합니다" % "파이썬") # 나는 파이썬을 좋아합니다 (str형)
print("Apple은 %c로 시작해요" % "A") # Apple은 A로 시작해요 (문자형 == char형)
print("나는 %s색과 %s색을 좋아해요" % ("파랑", "빨강")) # 두 개 이상의 str형 넣기

print("나는 {}살입니다".format(20)) # format() 안에 있는 값을 {}안에 넣음.
print("나는 {}색과 {}색을 좋아해요".format("파랑", "빨강"))
print("나는 {0}색과 {1}색을 좋아해요".format("초록", "분홍")) # 0번 index인 "초록", 1번 index인 "분홍"을 각각 넣음

print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨강")) # fotmat() 안의 변수를 가져다 쓰는 경우.

age = 25
color = "검정"
print(f"나는 {age}살이며, {color}색을 좋아해요") # 위에서 정의한 변수를 가져다 사용하는 경우

# 탈출 문자
print("백문이 불여일견\n백견이 불여일타")
print('저는 "재경" 입니다') # 문자열 내에 ""을 쓰려는 경우. " '' " 도 가능.
print("저는 \"재경\" 입니다") # "" 안에 \", \' 는 문자열 큰 따옴표로 인식함.
print("C:\\Users\\JaeGyeong") # 문장 내에서 \\는 \로 출력.
print("Red Apple\rPine") # \r : 커서를 맨 앞으로 이동하여 이동한 자리에서 \r뒷부분을 출력
print("Redd\bApple") # RedApple (backspace)
print("탭\t키 사용") # 탭 키

url = "http://naver.com"
str1 = url.replace("http://", "") # naver.com
str1 = str1[:str1.index(".")] # naver
password = str1[:3] + str(len(str1)) + str(str1.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다".format(url, password))

# 리스트
subway = [10, 20, 30]
subway = ["사람A", "사람B"]
print(subway)
subway.append("사람C")
print(subway) # ["사람A", "사람B", "사람C"]
subway.insert(1, "사람D") # 1번 index에 "사람D"를 넣음
print(subway) # ["사람A", "사람D" ... ]

print(subway.pop()) # 맨 뒤에 있는 값을 뽑아냄
print(subway) # 사람C는 없음.

subway.append("사람A")
print(subway.count("사람A")) # 2

num_list = [5,2,4,3,1]
num_list.sort() # 오름차순 정렬
print(num_list) # 1,2,3,4,5
num_list.reverse() # 순서 뒤집기 
print(num_list) # 5,4,3,2,1
num_list.clear() # 값을 지움
print(num_list) # []

num_list = [1, "사람", 2]
mix_list = ["사람", 3, "사람"]
num_list.extend(mix_list) # 값들을 합칩
print(num_list) # 1, "사람", 2, "사람", 3, "사람"

# 딕셔너리 
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3]) # 유재석
print(cabinet.get(3)) # 유재석
#print(cabinet[50]) # 오류 출력 및 프로그램 종료
print(cabinet.get(50)) # None 출력
print(cabinet.get(50, "비어 있음")) # 값이 없을 경우 오른쪽 문자열을 출력
print(3 in cabinet) # 3이라는 키가 cabinet에 있는가? 있으면 True, 없으면 False

cabinet = {"A-3":"정형돈", "B-100":"조세호"} # 문자열도 키로 사용 가능
cabinet["C-20"] = "정준하" # C-20 이라는 키를 생성하고 그 안에 값을 넣음
print(cabinet)
del cabinet["A-3"] # 키 A-3 을 삭제
print(cabinet) # {'B-100': '조세호', 'C-20': '정준하'}
print(cabinet.keys()) # 키 들만 출력
print(cabinet.values()) # 값 들만 출력
print(cabinet.items()) # 키와 값들을 출력 : dict_items([('B-100', '조세호'), ('C-20', '정준하')])
cabinet.clear() # cabinet 안 키와 값들을 삭제 : {}

# 튜플
menu = ("돈까스", "치즈까스")
print(menu[0]) # 돈까스
 # 튜플은 add() 를 지원하지 않음.
(name, age, hobby) = ("김선생", 25, "축구")
print(name, age, hobby)

# 집합(set) : 중복이 없고 순서가 없음
my_set = {1,2,3,3,3}
print(my_set) # 1, 2, 3

java = {"윤", "김", "태"}
cplusplus = set(["윤", "박"])
print(java & cplusplus) # 윤 (교집합 출력) 
print(java.intersection(cplusplus)) # 위와 같음
print(java | cplusplus) # 윤, 김, 태, 박 (합집합, 순서는 무작위)
print(java.union(cplusplus)) # 위와 같음
print(java - cplusplus) # 김, 태, 박 (차집합)
print(java.difference(cplusplus)) # 위와 같음
java.add("박") # set에 값 추가
print(java) # 윤, 김, 태 ,박
java.remove("윤") # set에서 값 제거
print(java) # 김, 태, 박

# 자료 구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # {'우유', '주스', '커피'} <class 'set'>
menu = list(menu)
print(menu, type(menu)) # ['주스', '우유', '커피'] <class 'list'>
menu = tuple(menu)
print(menu, type(menu)) # ('주스', '우유', '커피') <class 'tuple'>
menu = set(menu)
print(menu, type(menu)) # {'주스', '우유', '커피'} <class 'set'>

# random 모듈
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst) # 무작위로 섞음
print(lst)
print(sample(lst, 2)) # lst에서 무작위로 2개 값을 뽑음

# 추첨기
from random import *
users = range(1, 21) # 1부터 20까지의 수 생성. 단, type이 range임.
users = list(users)
shuffle(users)

winners = sample(users, 4)

print(" -- 당첨자 발표 -- ")
print(" 치킨 당첨자 : {0}".format(winners[0]))
print(" 커피 당첨자 : {0}".format(winners[1:]))

# if
weather = "미세먼지" # input("") 사용자 입력값을 받음.
if weather == "비" or "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30: # 10 <= temp < 30 도 가능
    print("괜찮은 날씨네요")
elif 0 <= temp and temp < 10: # 0 <= temp < 10 도 가능
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")

    

