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
        #A is kept as acc which will not change when its correct choice but accb needs to be updated
        #account a will change in further if else where accounta = accountb
        accountb=get_ran_account()
        
        while accounta==accountb:#ensures account b wont be equal to account a
            accountb=random.choice(data)
        print(f"Compare A : {formatstring(accounta)}")
        print(f"Against B : {formatstring(accountb)}")
        
        guess=input("Select who has more followers, A or B:").lower()
        rguess=rightguess(accounta,accountb,guess)
        
        #if rightgues function returns True or could also write rguess==guess
        if rguess:
            score=score +1
            print(f"You're right, current score is {score}")
            
            '''now to make it so that the at scores 1,3,5... correct data remains and 
            others wrong data remains, i.e alternatively change data which is to be compared with'''
            if score%2==1:#when score is 1,3,5...
                if guess=="b":#when obviously(cause its in that block) guess is right "odd times/first time" & its b
                  accounta=accountb#where account b is the winner
                else:
                    pass #when guess a will be right "on odd number score/first times" it will remain as it is 
            else:#only execute if score ever becomes 2,4,6...
                '''when guess a or b is right on second time,"second time" 
                meaning when score will be 2,4,6 i.e this else block will be executed 
                alternatively if guesses will be continously right '''
                if guess=="a":
                    accounta=accountb
                else:
                    pass #when guess b is right second time then wrong data i.e 'a' will remain and b will be randomized
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

