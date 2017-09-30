class maths:
    def findHCF(self,number1, number2):
        smallest = min(number1,number2)
        for element in range(1,(smallest+1)):
            if (number1 % element == 0) and (number2 % element == 0):
                hcf = element
        return hcf

number1 = int(raw_input("Enter First Number: "))
number2 = int(raw_input("Enter Second Number: "))
object = maths()
print object.findHCF(number1,number2)