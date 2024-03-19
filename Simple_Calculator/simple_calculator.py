def calculator():
    print('Welcome to the simple calculator program')
    print("Input first number")
    number1= input()# prompt user to input a number
    print("Choose an operation +,-,*,/")
    a = input()# to input an operation choice
    print("Input second number ")
    number2= input()# prompt user to input a second number
    # using try , except for handling errors when user inputs a wrong input like string or any complex numbers.
    try:
        if  a == "+":
            print(float(number1)+float(number2))
        elif a== "-":
            print(float(number1)-float(number2))

        elif a== "/":
            print(float(number1)/float(number2))
        elif a=="*":
            print(float(number1)*float(number2))
        else:
            print("error, please choose a right operation")
    except :
        print('Input a valid number')
def main():
    while True:
        calculator()
        print('Want to perform another calcuation - yes/no')
        choice = input().lower()
        if choice == 'yes':
            continue
        elif choice == 'no':
            print('Thank you')
            break
        else:
            print('no right choice entered,Thank you for using ')
            break
if __name__ == "__main__":
    main()




    




 



    



