def bonAppetit(bill, k, b):
    total_to_pay = (sum(bill) - bill[k]) // 2

    if total_to_pay == b:
        print('Bon Appetit')
    else:
        print(b - total_to_pay)
