from random import randint
random_num = randint(1,100)
num = int(input("Enter a number: "))

attempts = 5
while random_num!= num and attempts>=0:
    num
    if num in range(random_num-10, random_num+10):
        if num> random_num:
            print("Little Bit High")
        elif num==random_num:
            print("You got it. That took {} attempts".format(attempts))
        else:
            print("Little bit low")
    
    else:
        if num> random_num:
            print("Too High")
        else: 
            print("Too Low")
    
    attempts += -1
    
    if attempts ==0:
        break

    num= int(input("You have {} attempts left".format(attempts)))
