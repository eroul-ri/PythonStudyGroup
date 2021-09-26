from sj_ATM.atm import account

atm = account()

while True:
    choice = input("1.입금  2.출금  3.송금  : ")
    if choice == "1":
        money = int(input("입금하실 금액을 넣어주세요. : "))
        atm.deposit(money)
        print("잔고는 %d 원입니다."%atm.balance)


    elif choice == "2":
        money = int(input("츨급하실 금액을 입력해주세요. : "))
        atm.withdrawal(money)
        print("잔고는 %d 원입니다."%atm.balance)

    elif choice == "3":
        opponentname = input("송금하실 상대방 이름을 입력해주세요. : ")
        opponentaccountNum = input("계좌를 입력해주세요. : ")
        money = int(input("송금할 금액을 입격해주세요. : "))
        atm.transfer(opponentname, opponentaccountNum, money)
        print("잔고는 %d 원입니다."%atm.balance)


