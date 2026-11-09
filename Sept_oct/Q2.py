


n1 = int(input("Enter the first number :- "))
n2 = int(input("Enter the second number:-")) 
operator = input("Enter the operator (+,-*,/,%)")
match operator:
        case "+":
                result1 = n1 + n2
                print(result1)
        case "-":
                result1 = n1 - n2
                print(result1)
        case "*":
                result2 = n1 * n2
                print(result2)
        case "/":
                result2 = n1 / n2
                print(result2)
        case "%":
                result2 = n1 % n2
                print(result2)
        case _ :
                print("Invalid operator")