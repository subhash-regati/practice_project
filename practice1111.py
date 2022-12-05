amount=1299
try:
    if amount<2999:
        raise ValueError('please increase the amount')
    else:
        print('you are elgible')
except ValueError as e:
    print(e)