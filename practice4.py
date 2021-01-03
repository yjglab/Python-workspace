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
