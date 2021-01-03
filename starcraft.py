class Unit:
    def __init__(self, name, hp, speed): 
        self.name = name 
        self.hp = hp 
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, dmg):
        print("{0} : {1}데미지를 입었음.".format(self.name, dmg))
        self.hp -= dmg
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
        
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, dmg):
        Unit.__init__(self, name, hp, speed)
        self.dmg = dmg

    def attack(self, location):
        print("{0} : {1}방향으로 적을 공격함. [공격력 {2}]".format(self.name, location, self.dmg))

# 마린
class Marine(AttackUnit): 
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (체력 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))
class Tank(AttackUnit):
    seizeDeveloped = False # 초기 상태 : 팩토리에서 연구 필요

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seizeMode = False

    def setSeizeMode(self):
        if Tank.seizeDeveloped == False:
            return
        if self.seizeMode == False:
            print("{0} : 시즈 모드로 전환합니다.".format(self.name))
            self.dmg *= 2
            self.seizeMode = True
        else:
            print("{0} : 시즈 모드를 해제합니다.".format(self.name))
            self.dmg /= 2
            self.seizeMode = False

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

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True: 
            print("{0} : 클로킹 모드 해제".format(self.name))
            self.clocked == False
        else:
            print("{0} : 클로킹 모드 작동".format(self.name))
            self.clocked == True