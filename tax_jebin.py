print('Choose the case:')
print('1. Normal Case 2.Special Case')
case = int(input())

if case == 1:
    print('Input the total ammount of money: ')
    inputMoney = float(input())

    if inputMoney > 1600000:
        num = inputMoney - 1600000
        tax1 = num * (25 / 100)
        totalTax = tax1 + 195000
        print(totalTax)
    elif inputMoney >= 1100000 and inputMoney < 1600000:
        num = inputMoney - 1100000
        tax1 = num * (20 / 100)
        totalTax = tax1 + 95000
        print(totalTax)
    elif inputMoney >= 700000 and inputMoney < 1100000:
        num = inputMoney - 700000
        tax1 = num * (15 / 100)
        totalTax = tax1 + 35000
        print(totalTax)
    elif inputMoney >= 400000 and inputMoney < 700000:
        num = inputMoney - 400000
        tax1 = num * (10 / 100)
        totalTax = tax1 + 5000
        print(totalTax)
    elif inputMoney >= 300000 and inputMoney < 400000:
        num = inputMoney - 300000
        tax1 = num * (5 / 100)
        totalTax = tax1
        print(totalTax)
    else:
        totalTax = 0
        print(totalTax)
elif case == 2:

    print('Input the total ammount of money: ')
    inputMoney = float(input())

    print('Choose the special case from below')
    print('1. Woman and citizen with age > 65')
    print('2. Disabled')
    print('3. Parents of disabled')
    print('4. Wounded freedom fighters')

    caseE = int(input())
    if caseE == 1:
        if inputMoney > 1600000:
            num = inputMoney - 1600000
            tax1 = num * (25 / 100)
            totalTax = tax1 + 195000
            print(totalTax)
        elif inputMoney >= 1100000 and inputMoney < 1600000:
            num = inputMoney - 1100000
            tax1 = num * (20 / 100)
            totalTax = tax1 + 95000
            print(totalTax)
        elif inputMoney >= 700000 and inputMoney < 1100000:
            num = inputMoney - 700000
            tax1 = num * (15 / 100)
            totalTax = tax1 + 35000
            print(totalTax)
        elif inputMoney >= 400000 and inputMoney < 700000:
            num = inputMoney - 400000
            tax1 = num * (10 / 100)
            totalTax = tax1 + 5000
            print(totalTax)
        elif inputMoney >= 350000 and inputMoney < 400000:
            num = inputMoney - 350000
            tax1 = num * (5 / 100)
            totalTax = tax1
            print(totalTax)
        else:
            totalTax = 0
            print(totalTax)

    elif caseE == 2:
        if inputMoney > 1600000:
            num = inputMoney - 1600000
            tax1 = num * (25 / 100)
            totalTax = tax1 + 195000
            print(totalTax)
        elif inputMoney >= 1100000 and inputMoney < 1600000:
            num = inputMoney - 1100000
            tax1 = num * (20 / 100)
            totalTax = tax1 + 95000
            print(totalTax)
        elif inputMoney >= 700000 and inputMoney < 1100000:
            num = inputMoney - 700000
            tax1 = num * (15 / 100)
            totalTax = tax1 + 35000
            print(totalTax)
        elif inputMoney >= 450000 and inputMoney < 700000:
            num = inputMoney - 450000
            tax1 = num * (10 / 100)
            totalTax = tax1 + 5000
            print(totalTax)
        else:
            totalTax = 0
            print(totalTax)

    elif caseE == 3:
        if inputMoney > 1600000:
            num = inputMoney - 1600000
            tax1 = num * (25 / 100)
            totalTax = tax1 + 195000
            print(totalTax)
        elif inputMoney >= 1100000 and inputMoney < 1600000:
            num = inputMoney - 1100000
            tax1 = num * (20 / 100)
            totalTax = tax1 + 95000
            print(totalTax)
        elif inputMoney >= 700000 and inputMoney < 1100000:
            num = inputMoney - 700000
            tax1 = num * (15 / 100)
            totalTax = tax1 + 35000
            print(totalTax)
        elif inputMoney >= 400000 and inputMoney < 700000:
            num = inputMoney - 400000
            tax1 = num * (10 / 100)
            totalTax = tax1 + 5000
            print(totalTax)
        elif inputMoney >= 350000 and inputMoney < 400000:
            num = inputMoney - 350000
            tax1 = num * (5 / 100)
            totalTax = tax1
            print(totalTax)
        else:
            totalTax = 0
            print(totalTax)


    else:
        if inputMoney > 1600000:
            num = inputMoney - 1600000
            tax1 = num * (25 / 100)
            totalTax = tax1 + 195000
            print(totalTax)
        elif inputMoney >= 1100000 and inputMoney < 1600000:
            num = inputMoney - 1100000
            tax1 = num * (20 / 100)
            totalTax = tax1 + 95000
            print(totalTax)
        elif inputMoney >= 700000 and inputMoney < 1100000:
            num = inputMoney - 700000
            tax1 = num * (15 / 100)
            totalTax = tax1 + 35000
            print(totalTax)
        elif inputMoney >= 475000 and inputMoney < 700000:
            num = inputMoney - 475000
            tax1 = num * (10 / 100)
            totalTax = tax1 + 5000
            print(totalTax)
        else:
            totalTax = 0
            print(totalTax)