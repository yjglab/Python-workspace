### 모듈 : 필요한 함수 정의 ,클래스 등의 파일을 모은 것.

# ex. 영화 일반가격
def price(people):
    print("{0}명분 가격은 {1}원 입니다.".format(people, people * 10000))
# ex. 영화 조조가격
def priceMorning(people):
    print("{0}명분 조조 할인 가격은 {1}원 입니다.".format(people, people * 6000))
# ex. 영화 군인가격
def priceSoldier(people):
    print("{0}명분 군인 할인 가격은 {1}원 입니다.".format(people, people * 4000))