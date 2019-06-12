
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
    #maked two different except for print error
    #as - is a alias
except ZeroDivisionError as err:
    #used alias for print
    print(err)
except ValueError:
    print("Invalid input")
