# 테스트
def calculate_change(payment, cost):
    change = payment - cost
    five_man = int(change/50000)
    change = change - five_man*50000
    man = int(change/10000)
    change=change-man*10000
    oh_chun = int(change/5000)
    change=change-oh_chun*5000
    chun=int(change/1000)



    print("50000원 지폐: {}장".format(five_man))
    print("10000원 지폐: {}장".format(man))
    print("5000원 지폐: {}장".format(oh_chun))
    print("1000원 지폐: {}장".format(chun))
    return change
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)


print("-----------------")
def calculate_change_with_for(payment, cost):
    change = payment - cost
    money_list=[50000, 10000, 5000, 1000]
    money_number=[]
    for i in money_list:
        k=0
        number=int(change/i)
        money_number.append(number)
        change-=i*number
        print("{}원 지폐: {}장".format(money_list[k] ,number))
        k+=1

calculate_change_with_for(100000, 33000)