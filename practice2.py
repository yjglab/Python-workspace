# for

for waitingNum in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waitingNum)) # 0부터 4까지 값을 넣은 반복

for waitingNum in range(7): # range(1, 6) 은 1부터 6전까지
    print("다음번호 : {0}".format(waitingNum)) # 0부터 7전까지

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}님, 커피가 준비되었습니다".format(customer))

# while : while 내 조건이 만족할 때까지 반복
customer = "토르"
index = 5
while index >= 1:
    print("{0}님, 쿠폰 사용했습니다. {1}장 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("쿠폰을 모두 사용했습니다.")

'''
customer = "헐크"
index = 1
while True:
    print("{0}님, 홍차 나왔습니다. 호출 {1}회".format(customer, index))
    index += 1 
''' # 무한 루프. 빠져나가려면 Ctrl + C

'''
customer = "윌슨"
person = "Unknown"

while person != customer :
    print("{0}님 우유 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?") # 윌슨을 입력할 때 까지 반복함. 
'''


# continue 와 break
absent = [2, 5]
noBook = [7]
for student in range(1, 11):
    if student in absent:
        continue # continue 작동 시 다음 줄로 가지 않고 그다음 반복을 실행함
    elif student in noBook:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break # 반복문 탈출
    print("{0}아, 책을 읽어봐".format(student))

students = [1,2,3,4,5]
students = [i + 100 for i in students]
print(students) # [101, 102, 103, 104, 105]

students = ["james", "max", "honey"]
students = [len(i) for i in students] 
print(students) # [5, 3, 5]

students = ["kerly", "forme", "jane"]
students = [i.upper() for i in students]
print(students) # ['KERLY', 'FORME', 'JANE']


from random import *

cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time < 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분".format(i, time))

print("총 탑승 승객 : {0} 분".format(cnt))


# 함수
def openAccount():
    print("A")

def deposit(balance, money):
    print("입금 완료 / 잔액 : {0}".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금 완료 / 잔액 : {0}".format(balance - money))
        return balance - money
    else: 
        print("출금 실패 / 잔액 : {0}".format(balance))
        return balance

def withdrawNight(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
print(balance) # 1000
balance = withdraw(balance, 2000) # 출금 실패 / 잔액 : 1000
balance = withdraw(balance, 500) # 출금 완료 / 잔액 : 500

commission, balance = withdrawNight(balance, 300)
print("수수료는 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance)) # 수수료는 100원이며, 잔액은 100원 입니다.


# 기본값

def profile(name, age, mainLanguage):
    print("이름 : {0}\t나이 : {1}\t주 언어 : {2}"\
        .format(name, age, mainLanguage)) # \ : 코드 상에서 줄바꿈

profile("잭영", 20, "파이썬")

def profile2(name, age=17, mainLanguage="Python"): # age와 mainLanguage 값을 전달받지 않는 경우, 입력된 기본값으로 들어감
    print("이름 : {0}\t나이 : {1}\t주 언어 : {2}"\
        .format(name, age, mainLanguage))

profile2("제임스")


# 키워드 값을 통한 함수 호출

def profile3(name, age, mainLanguage):
    print(name, age, mainLanguage)

profile3(name="병진", mainLanguage="자바스크립트", age=25) # 매개변수값을 키워드를 이용해 호출. 순서도 상관없음.


# 가변인자를 통한 함수 호출
  # 가변인자를 쓰지 않을 때 -
def profile4(name, age, lang1, lang2, lang3):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ") # end=" " 를 입력하면 줄바꿈이 되지 않음. 
    print(lang1, lang2, lang3)

profile4("젬스", 20, "python", "java", "c++") # 이름: 젬스      나이: 20         python java c++
profile4("땡뚜", 21, "Kotlin", "", "")  # 빈 값을 매번 입력해주어야 하는 번거로움 발생

  # 가변인자를 쓸 때 -
def profile5(name, age, *language):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ") 
    for lang in language:
        print(lang, end=" ")

profile5("좡즁", 25, "javascript", "C#")
print() # 줄바꿈.


# 전역 변수, 지역 변수

gun = 10

def checkpoint(soldiers): # 경계 근무 나가는 군인 수
    global gun # 전역 공간에 있는 gun 사용. global을 입력하지 않으면 지역변수로 계산하게 되는데 지역변수의 gun의 값이 할당되어 있지 않으므로 에러.
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun)) # 8

print("전체 총 : {0}".format(gun)) # 10
checkpoint(2)
print("남은 총 : {0}".format(gun)) # 8

# --
gun = 10

def checkpoint_ret(gun, soldiers): 
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun)) # 8
    return gun

print("전체 총 : {0}".format(gun)) # 10
gun = checkpoint_ret(gun, 2) # 전역 값 gun의 10을 함수에 넘기고 반환 값을 다시 전역 값 gun에 저장
print("남은 총 : {0}".format(gun)) # 8


# -- 

# def std_weight(height, gender):
#     height = height * (1/100)
#     if gender == "man":
#         weight = round(height * height * 22)
#     elif gender == "woman":
#         weight = round(height * height * 21)
#     return weight

# myKey = int(input("키 입력"))
# man1 = std_weight(myKey, "man")
# print("당신의 키: {0} 표준체중 : {1}".format(myKey, man1))

def std_weight(height, gender):
    if gender == "man":
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "man"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다".format(height, gender, weight))


# 표준 입출력 
print("A", "B", sep=",") # sep은 둘 사이를 어떻게 처리할 지를 결정. # A,B
print("A", "B", "C", sep=" vs ") # A vs B vs C

print("A", "B", sep=",", end="?") # end는 문장의 끝부분을 어떻게 처리할 지를 결정
print("무슨 알파벳입니까") # A,B?무슨 알파벳입니까

import sys
print("C", "D", file=sys.stdout) # 표준 출력
print("C", "D", file=sys.stderr) # 표준 에러

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject, score) # 수학 0\n영어 50\n코딩 100

for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":") 
    # ljust(8) : 총 8 칸의 공간을 확보한 상태로 왼쪽 정렬 
    # rjust(4) : 총 4 칸의 공간을 확보한 상태로 오른쪽 정렬


for num in range(1, 11):
    print("대기 번호 : " + str(num).zfill(3))
    # zfill(3) : 3개 만큼의 공간을 확보하고 빈 공간은 0으로 채움.

answer = input("값을 입력하시오 : ")
print("입력한 값은 " + answer + "입니다")