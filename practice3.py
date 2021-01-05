# 다양한 출력 포맷

print("{0: >10}".format(5252)) #       5252
# 빈 자리는 빈공간( )으로 두고, 오른쪽 정렬(>)을 하되, 총 10자리 공간 확보
print("{0: >+10}".format(333)) #       +333
print("{0: >+10}".format(-333)) #       -333
# 양수일 땐 +로 표시, 음수일 땐 -로 표시

print("{0:_<+10}".format(992)) # +992______
# 왼쪽 정렬하고 빈칸은 _로 채움.

print("{0:,}".format(100000000)) # 100,000,000
# 3자리 마다 콤마

print("{0:+,}".format(100000000)) # +100,000,000
# 3자리 마다 콤마, 부호도 붙임

print("{0:^<+30,}".format(100000000)) # +100,000,000^^^^^^^^^^^^^^^^^^
# 3자리 마다 콤마, 부호도 붙임, 자리 수(30)도 확보, 빈 칸은 ^ 로 채우기

print("{0:f}".format(5/3)) # 1.666667
# 소수점 출력

print("{0:.3f}".format(5/3)) # 1.667
# 소수점 특정 자리 수 까지만 표시. # 소수점 3자리에서 반올림함.


### 파일 입출력 
score_file = open("score.txt", "w", encoding="utf8") # w: write(쓰기용도)
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file2 = open("score.txt", "a", encoding="utf8") # a : append(내용추가)
score_file2.write("과학 : 80")
score_file2.write("\n코딩 : 100")
score_file2.close()

score_file3 = open("score.txt", "r", encoding="utf8") # r: read(파일 읽어오기)
print(score_file3.read()) # 수학 : 0\n영어 : 50\n과학 : 80\n코딩 : 100
score_file3.close()

score_file4 = open("score.txt", "r", encoding="utf8") 
print(score_file4.readline(), end="") # 줄별로 읽기, 한 줄 읽어오고 커서는 다음 줄로 이동
print(score_file4.readline(), end="")
print(score_file4.readline(), end="")
print(score_file4.readline(), end="")
score_file4.close()

print()

score_file5 = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file5.readline()
    if not line: # 읽어올 내용이 없다면
        break
    print(line, end="")
score_file5.close()

print()

score_file6 = open("score.txt", "r", encoding="utf8")
lines = score_file6.readlines() # 모든 줄을 읽어와 list 형태로 저장
for line in lines:
    print(line, end="")

score_file6.close()

print()

### pickle
# 프로그램상에서 우리가 사용하는 데이터를 파일 형태로 저장해줌. 다른 사람과 공유
# pickle에서는 바이너리 설정 필수, 인코딩 설정은 안해도 됨.
import pickle
profile_file = open("profile.pickle", "wb") # 쓰기모드, binery
profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile 내 정보를 profile_file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb") # 읽기모드, binery
profile = pickle.load(profile_file) # profile_file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()


### with
# 파일 열고 닫고 하는 작업을 더 편하게 할 수 있음
# 파일을 자동으로 닫아주어 close()를 사용하지 않아도 됨
import pickle

with open("profile.pickle", "rb") as profile_file: # 파일을 열고(open) 변수에 저장(as)
    print(pickle.load(profile_file))

# pickle 사용하지 않고 with 사용하기
with open("study.txt", "w", encoding="utf8") as study_file: # 쓰기
    study_file.write("파이썬 공부중")

with open("study.txt", "r", encoding="utf8") as study_file: # 읽기
    print(study_file.read()) # 파이썬 공부중


#--


for i in range(1, 4):
    with open(str(i) + "주차주간보고.txt", "w", encoding="utf8") as reportFile:
        reportFile.write("= {0}주차 주간 보고".format(i))
        reportFile.write("\n부서 : ")
        reportFile.write("\n이름 : ")
        reportFile.write("\n업무 요약 : ")


### 클래스
name = "marine"
hp = 40
dmg = 5
print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, dmg))

tankName = "탱크"
tankHP = 150
tankDmg = 35
print("{0} 유닛이 생성되었습니다.".format(tankName))
print("체력 {0}, 공격력 {1}\n".format(tankHP, tankDmg))

def attack(name, location, dmg):
    print("{0} : {1}방향으로 적을 공격합니다. [공격력 : {2}]".format( \
        name, location, dmg))

attack(name, "1시", dmg)
attack(tankName, "1시", tankDmg)

# 만들기
class Unit:
    def __init__(self, name, hp, dmg): # __init__ : 생성자. 객체
        self.name = name # 멤버 변수
        self.hp = hp # 멤버 변수
        self.dmg = dmg # 멤버 변수
        print("{0} 유닛이 생성됨.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.dmg))

print()
marine1 = Unit("마린", 40, 5) # 반드시 클래스 생성자에 정의된 개수(self제외)만큼 값을 보내야 함
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.dmg))

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 객체에 멤버 변수를 추가함.

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))


### 메소드 
class AttackUnit:
    def __init__(self, name, hp, dmg): # __init__ : 생성자. 객체
        self.name = name # 멤버 변수
        self.hp = hp # 멤버 변수
        self.dmg = dmg # 멤버 변수
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적을 공격합니다. [공격력 : {2}]"\
            .format(self.name, location, self.dmg))
    
    def damaged(self, dmg):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, dmg))
        self.hp -= dmg
        print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 이 유닛은 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)


### 상속
class Unit2:
    def __init__(self, name, hp): 
        self.name = name 
        self.hp = hp 

class AttackUnit2(Unit2): # Unit2 클래스를 상속받음. Unit2는 부모 클래스, AttackUnit2는 자식 클래스가 됨.
    def __init__(self, name, hp, dmg): 
        Unit2.__init__(self, name, hp) # Unit2 에서 만들어진 생성자를 호출하여 name과 hp를 정의할 수 있음
        self.dmg = dmg

print()
firebat2 = AttackUnit("파이어뱃2", 50, 16)
firebat2.attack("5시")
firebat2.damaged(25)
firebat2.damaged(25)


