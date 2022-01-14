import art
import replit
#adding
def add (n1, n2):
        return n1+n2

#substracting
def substract (n1, n2):
        return n1-n2

#multiplying
def multiply (n1, n2):
        return n1*n2

#dividing
def divide (n1, n2):
        return n1/n2

operations = {
"+" : add,
"-" : substract,
"*" : multiply,
"/" : divide


}
def calculator():
        again = "y"
        print(art.logo)
        num1 = float(input("What is the first number? "))
        while again =="y":
                for key in operations:
                        print(key)
                symbol = input("What operation do you choose?: ")
                if symbol not in operations:
                        print ("wrong input")
                else:
                        num2 = float(input("What is the next number? "))
                        calculation = operations.get(symbol, "wrong input")
                        answear = calculation(num1,num2)

                        print (f"{num1} {symbol} {num2} = {answear}")

                        again = input (f"Do you want to perform another calculation on the result ({answear})? Click y if yes, n to start again, click any button to exit: ")

                        num1=answear
        

        while again == "n":
                replit.clear()
                calculator()
        else:
                return
calculator ()