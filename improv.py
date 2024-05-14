from game_data import data
from art import logo, vs
import random

# leave user actions to later and focus on functions first
''''''

#from game_data choose randomdata & 
def get_ran_account():
    return random.choice(data)
##'print those two "unique" random data' but only for first time, if won the {guess} will remain 
'''as you can see many operations are being performed for this so this will be under one big function such as game
and a action with a condition(like the one in single qoutes) should have seperate function like formatstring()'''
def game():
    score=0
    accounta=get_ran_account()

    gameis=True

    while gameis:
        #A is kept as acc which will not change when is correct choice but accb needs to be updated
        accountb=get_ran_account()
        
        while accounta==accountb:
            accountb=random.choice(data)
        print(f"Compare A : {formatstring(accounta)}")
        print(f"Against B : {formatstring(accountb)}")
        
        guess=input("Select who has more followers, A or B:").lower()
        rguess=rightguess(accounta,accountb,guess)
        
        #if rightgues function returns True or could also write rguess==guess
        if rguess:
            score=score +1
            print(f"You're right, current score is {score}")
            
            #now to make it so that the correct data remains
            if guess=="b":#this to make sure if guess b is correct it shouldnt be updated
                accounta=accountb
        else:
            print(f"You lose, your final score is {score}")
    

def formatstring(acc):
    name=acc["name"]
    desc=acc["description"]
    return f"name: {name}, {desc}"
    
#(guess) return which option is 'right/has more followers'
# def rightguess(a,b,guess):
#     if guess=="a":
#         if a["follower_count"]>b["follower_count"]:
#             return "a"
#         else:
#             return False
#     elif guess=="b":
#          if b["follower_count"]>a["follower_count"]:
#              return "b"
#          else:
#              return False
#     else:
#         pass

'''The above code could be further improved by using the knowledge that if
guess="a"    and check if guess=="a" not "b" '''


# def rightguess(a,b,guess):
#     #Returns True or False
#     if a["follower_count"]>b["follower_count"]:
#         return guess=="a"# if when calling function guess="b", it'll be false
        
#     if b["follower_count"]>a["follower_count"]:              
#         return guess=="b"

#ORR 
def rightguess(account_a, account_b, guess):
    followers_a = account_a["follower_count"]
    followers_b = account_b["follower_count"]
    return (guess == "a" and followers_a > followers_b) or (guess == "b" and followers_b > followers_a)

        

game()
    


#create interface for user to check that they are right {and display score} 
##guess a or b:

#compare the data (to further decide if player is correct) 

