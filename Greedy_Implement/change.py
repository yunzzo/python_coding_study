#입력과 선언
change=int(input("거스름돈을 입력하세요:"))
count =0
coin_types=[500,100,50,10]

#처리
for coin in coin_types:
    print(coin)
    count += change//coin
    change %= coin


#출력
print(count)

#공부를 하다보니 실제 자동 자판기의 경우가 생각났다. 실제 자동 자판기의 경우에는, 
#1 거스름돈을 계산하는 과정(투입된 돈 - 구매한 상품의 가격)
#2 화폐의 종류 뿐 아니라, 남아있는 동전의 개수까지 고려해서 거스름돈을 거슬러주는 과정까지

