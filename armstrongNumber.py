number = raw_input("enter number: ")
order = raw_input("Enter order: ")

orderList=list()
splitNumber = list(number)   #[1364]
for num in splitNumber:
    ans = int(num)**int(order)
    orderList.append(ans)

result= sum(orderList)
if result == int(number):
    print "Number is Armstrong"
else:
    print "Number is not Armstrong"