### 모듈

import theater_module # 파일명만 입력하여 모듈 가져옴
theater_module.price(3) # 인원 3명의 일반가격/ 출력: 3명분 가격은 30000원 입니다.
theater_module.priceMorning(4) # 인원 4명의 조조가격/ 출력: 4명분 조조 할인 가격은 24000원 입니다.
theater_module.priceSoldier(5) # 인원 5명의 군인가격/ 출력: 5명분 군인 할인 가격은 20000원 입니다.

import theater_module as mv # theater_module를 mv라는 별칭을 붙임
mv.price(3) # theater_module.price(3)과 같음

from theater_module import * # theater_module에 관한 모든 것을 사용
price(3) # 위와 같음

from theater_module import price, priceMorning # 특정 함수만 가져옴
price(5)
priceMorning(6)
# priceSoldier는 사용 불가

from theater_module import priceSoldier as price
price(2) # 2명분 군인 할인 가격은 8000원 입니다. # theater_module의 price함수가 아님. 