main.py is entirely code written from scratch

instructers.py is from instructer of the course i am doing and i changed it a bit so that instead of always  A to be same account , rigtht guess should be A

improv.py is my second try to create clean code 

tips:
option must be easily decided if right or wrong by using code like 
//
gess=input("whats ur guess")

if rightguess(option1,option2,gess):
#where rightquess retruns true or false

def rightguess(option1,option2,gess):
return (option1==gess and option1>option2) or (option2==gess and option1<option2) 