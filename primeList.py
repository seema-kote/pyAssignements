startNum=int(raw_input("Enter Start number: "))
endNum=int(raw_input("Enter End number: "))

numberIsPrime=True;
for number in range(startNum,(endNum+1)):
    numberIsPrime=True
    for num in range(2,number):
        if number%num == 0:
           numberIsPrime= False
        break
    if numberIsPrime==False:
        continue
    else:
        print number