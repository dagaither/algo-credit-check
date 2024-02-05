singles = []

def credit_check(str):

    for num in str[-1::-2]:
        singles.append(int(num))

    for num in str[-2::-2]:
        num = int(num) * 2

        if num < 9:
            singles.append(num)
        else:
            num = ((num //10) + (num %10))
            singles.append(num)

    if (sum(singles)) % 10 == 0:
        return "The number is valid!"
    
    else:
        return "The number is invalid!"
        