import random

def change(remain):#거스름돈을 500원 100원 50원 10원 단이로 나오게 하는 함수임
  # remain: 거스름돈 금액
  # return: 거스름돈의 500원, 100원, 50원, 10원 개수

  coin_500 = remain // 500
  coin_100 = (remain % 500) // 100
  coin_50 = (remain % 100) // 50
  coin_10 = (remain % 50) // 10
  return "거스름돈 500원 : {}, 100원 : {}, 50원 : {}, 10원 : {}".format(coin_500, coin_100, coin_50, coin_10)

products = {
  '1.칠성사이다':1870,
  '2.코카콜라':6010,
  '3.비타500':780,
  '4.몬스터':2090,
  '5.피크닉':3110,
  '6.랜덤 음료수':2100,
  '7.자몽에이드':2500,
  '8.오렌지주스':2800,
  '9.토마토주스':3000,
  '10.사과주스':2700
}

# products: 제품 목록
# key: 제품 이름
# value: 제품 가격

for i in products:
  print("--------------------------------------")
  print(i,products[i])

goods_name=list(products.keys())
goods_price=list(products.values())

# goods_name: 제품 이름 목록
# goods_price: 제품 가격 목록

coin = int(input('동전을 넣어주세요 : '))    # 동전을 입력 받음

while True : 
  print("현재잔액 : " ,coin)          # 현재 잔액을 알려줌
  select = int(input('(0번을 누르면 환산됩니다.)\n원하는 제품을 선택하세요 : '))-1 #원하는 제품을 입력
  if select == 6:
    # 랜덤 음료수 선택
    random_number = random.randint(1, 6)#1부터 5까지의 랜덤 음료수가 나옴
    print(random_number)
    if random_number == -1 : 
      break
    elif random_number >= 0 and random_number <=5: 
      coin = coin - goods_price[random_number]
    else : 
      print('**********************')
      print("\n다른 숫자하삼\n")#다른 숫자를 하라고 알려줌
      continue

  if select == -1 : # 0이면 끝남
    break

  elif select >= 0 and select <=10 : #0하고 10라면 
    coin = coin - goods_price[select] #제품의 가격을 원래 있던 돈에서 빼줌

    if coin<0 :
      coin = coin + goods_price[select] #코인이 제품보다 적을 경우 돈을 더 넣으라고 알려줌
      print("돈을 더 넣고 다시 실행 해 주세요.")
      break
    else : 
      print("%s 이(가) 나왔습니다" % goods_name[select])#제품이 나왔다고 알려줌

    if select != 6 : 
      # 할인
      discount = random.randint(0, 100)
      if discount >= 0 and discount <= 100 : 
        discount_price = goods_price[select] * discount / 100
        coin = coin + discount_price
        print("할인된 금액은 {}원입니다.".format(discount_price))

  
  
print("--------------------------")
print("고객님의 거스름돈은 {}원입니다.".format(change(coin)))
