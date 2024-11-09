from random import randint
from game_data import data


a=data[randint(0,len(data)-1)]
b=data[randint(0,len(data)-1)]
followers_a = a["follower_count"]
followers_b = b["follower_count"]
c= True
score = 0
while c:
    print("Who do you think has got more followers", a["name"], "or", b["name"])
    user_answer = input("Type A or B: ").lower()
    if followers_a > followers_b and user_answer == "a":
        score +=1
        print("That's right! Current score: ", score)
        a=b
        b=data[randint(0,len(data)-1)]


    elif followers_b> followers_a and user_answer == "b":
        score+=1
        print("That's right! Current score: ", score)
        b=a
        a= data[randint(0,len(data)-1)]
    else:
        print("You lost. Your score is: ",score )
        c= False
# for username in data:
#     data["name"]
    
