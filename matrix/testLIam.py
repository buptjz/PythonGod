def rental_car_cost(days):
    moneyindays=40
    if days==1:
        pass
    elif days == 2:
        pass
    elif days >= 3 and days < 7:
        pass
    elif days >= 7:
        pass
    else:
        return 0
    
def rental_car_cost2(days):
    moneyindays=40
    if days>0:
        days=days*moneyindays
    if days==1:
        moneyindays=40
        return moneyindays
    elif days == 2:
        moneyindays = 80
        return moneyindays        
    elif days >= 3:
        moneyindays -= 20
        return moneyindays
    elif days >= 7:
        moneyindays=moneyindays-50
        return moneyindays
    else:
        return 0
print(rental_car_cost2(1))