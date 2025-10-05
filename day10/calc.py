print("""
    _____________________       ██████╗ █████╗ ██╗      ██████╗
   |  _________________  |      ██╔══██╗██╔══██╗██║     ██╔═══██╗
   | |              0. | |      ██████╔╝███████║██║     ██║   ██║
   | |_________________| |      ██╔═══╝ ██╔══██║██║     ██║   ██║
   |  ___ ___ ___   ___  |      ██║     ██║  ██║███████╗╚██████╔╝
   | | 7 | 8 | 9 | | + | |      ╚═╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝
   | |___|___|___| |___| |
   | | 4 | 5 | 6 | | - | |
   | |___|___|___| |___| |
   | | 1 | 2 | 3 | | x | |
   | |___|___|___| |___| |
   | | . | 0 | = | | ÷ | |
   | |___|___|___| |___| |
   |_____________________|
""")

def add(n1,n2):
    return n1+n2

def substract(n1,n2):
    return n1-n2


def multiply(n1,n2):
    return n1*n2


def devide(n1,n2):
    return n1/n2


operations = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":devide,
}

should_continue = True
nn1 = float(input("Enter first number: "))


while should_continue:
    nn2= float(input("Enter second number: "))
    operator = input("Enter operator: ")
    ans = operations[operator](nn1,nn2)
    print(f"{nn1}{operator}{nn2}={ans}")

    choice = input(f"type y to cotinue with {ans}, or type n to start a new calculation:, or type any to exit:")

    if choice=="y":
         nn1=ans
    elif choice=="n":
        nn1 = float(input("Enter first number: "))
    else:
        exit()