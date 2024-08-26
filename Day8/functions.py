def prime_checker(number):
    if number%2 == 0:
        print("It's not a prime number")
    else:
        print ('It is a prime number')

n= int(input("Check this number: "))
prime_checker(number=n)