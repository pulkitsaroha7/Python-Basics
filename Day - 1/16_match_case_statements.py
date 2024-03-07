a = int(input("Enter the value : "))
match(a):
    case _ if a < 0:
        print("default case 0 , ",a,"is not a positive number")
    case _ if a < 10:
        print("default case 1 , ",a,"is greater than 0 and less than 10")
    case _ if a < 20:
        print("default case 2 , ",a,"is greater than 10 and less than 20")
    case _ if a < 30:
        print("default case 3 , ",a,"is greater than 20 and less than 30")
    case _ if a > 30:
        print("default case 4 , ",a,"is greater than 30")