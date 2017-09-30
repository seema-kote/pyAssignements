# Author name : Kote Seema M ('https://github.com/seema-kote/')
# Created Date : 12th Sep 2017

startNum = raw_input("Enter Start number: ")
endNum = raw_input("Enter End number: ")
for number in range(int(startNum),(int(endNum)+1)):
    order = len(str(number))
    if order == 1:
        continue
    splitNumber = list(str(number))
    orderList =[]
    for num in splitNumber:
        ans = int(num)**int(order)
        orderList.append(ans)
    result = sum(orderList)
    if result == int(number):
        print "{0} Number is Armstrong".format(number)
    else:
        continue




