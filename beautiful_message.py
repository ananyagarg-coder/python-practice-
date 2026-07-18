print("You are beautiful")
believe = input("Do you believe it? ")


def is_tell(n):
    while n!=0:
        print("You are beautiful")
        n = n-1


def is_yes(y):
    if y == 'yes':
        print("It's good to know that")
    else:
        print("Oh!, let me tell you how much beautiful you are")
        a = int(input("How many times you wanna hear you are beautiful? ")
        print(is_tell(a))

is_yes(believe)

 
