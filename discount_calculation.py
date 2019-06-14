price = float(input('enter de price of product: '))
disc = int(input('report discount percentage: '))

result1 = price*disc/100
result2 = price-result1

print('the discont is ${}'.format(result2))