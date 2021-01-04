### 다중상속

class Unit:
    def __init__(self, name, hp, speed): 
        self.name = name 
        self.hp = hp 
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
        
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, dmg):
        Unit.__init__(self, name, hp, speed)
        self.dmg = dmg

    def attack(self, location):
        print("{0} : {1}방향으로 적을 공격함. [공격력 {2}]".format(self.name, location, self.dmg))

    def damaged(self, dmg):
        print("{0} : {1}데미지를 입었음.".format(self.name, dmg))
        self.hp -= dmg
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

class Flyable:
    def __init__(self, flySpeed):
        self.flySpeed = flySpeed

    def fly(self, name, location):
        print("{0} : {1}방향으로 비행합니다. [비행속도 : {2}]"\
            .format(name, location, self.flySpeed))

class FlyableAttackUnit(AttackUnit, Flyable): # AttackUnit 클래스와 Flyable 클래스를 모두 상속받음
    def __init__(self, name, hp, dmg, flySpeed):
        AttackUnit.__init__(self, name, hp, 0, dmg) # 0은 지상 유닛 speed에 해당
        Flyable.__init__(self, flySpeed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

vulture = AttackUnit("벌쳐", 80, 10, 20)
battleCruiser = FlyableAttackUnit("배틀크루져", 500, 25, 3)

vulture.move("11시")
# battleCruiser.fly(battleCruiser.name, "9시")
battleCruiser.move("9시")


### pass : 아무것도 안하고 일단 넘어감
### super 

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0) # 건물은 스피드 0
        super().__init__(name, hp, 0) # super를 통해 초기화할 때는 self 정보를 넣지 않음. 내용은 윗줄과 동일.
        self.location = location

supplyDepot = BuildingUnit("서플라이 디폿", 500, "7시")

# super를 통해서는 다중 상속이 어려움
class A:
    def __init__(self):
        print("나는 A다")

class B:
    def __init__(self):
        print("나는 B다")

class C(A, B): # B, A로 상속 순서를 바꾸면 밑에서 # '나는 B다' 가 출력될 것임.
    def __init__(self):
        super().__init__()

alphabet = C() # 나는 A다


#--

class House:
    def __init__(self, location, houseType, dealType, price, completionYear):
        self.location = location
        self.houseType = houseType
        self.dealType = dealType
        self.price = price
        self.completionYear = completionYear

    def showDetail(self):
        print(self.location, self.houseType, self.dealType, self.price, self.completionYear)

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("이태원", "빌라", "전세", "5억", "2007년")
houses.append(house1)
houses.append(house2)

print("총 {0}대의 매물이 있습니다".format(len(houses)))
for house in houses:   
    house.showDetail()


### 예외 처리
try: 
    print("나누기 전용 계산기")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError: # 숫자가 아닌 값을 넣었을 때 처리
    print("에러! 잘못된 값을 입력함") # 에러가 발생하면 이 문장을 출력함
except ZeroDivisionError as err: # 숫자를 0으로 나누었을 때 처리
    print(err) # division by zero
except Exception as err: # IndexError 대신 그냥 except로 처리도 가능
    print("알 수 없는 오류 발생") # ValueError나 ZeroDivisionError가 아닌 모든 에러에 대하여 처리
    print(err)

### 에러 발생시키기 ,사용자 정의 에러
class BigNumberError(Exception):
    def __init__(self, errorMsg):
        self.errorMsg = errorMsg
    
    def __str__(self):
        return self.errorMsg

try:
    print("한 자리 숫자 나누기 전용계산기")
    num1 = int(input("첫 수 입력"))
    num2 = int(input("두 수 입력"))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except BigNumberError as err:
    print("에러 발생. 한 자리 수만 입력하세요.")
    print(err) # 입력값 : {0}, {1}

finally: # 위 코드가 정상적이건, 오류이건 반드시 출력되는 구문
    print("계산기를 이용해주셔서 감사합니다")


#--
class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1
while(True):
    try:
        print("[남은 치킨 : {0}".format(chicken))
        order = int(input("치킨을 몇 마리 주문하시나요?"))
        if order > chicken:
            print("재료가 부족합니다")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 : {0}] {1}마리 주문 완료".format(waiting, order))
            waiting += 1
            chicken -= order
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력했습니다")
    except SoldOutError:
        print("재고 소진")
        break
