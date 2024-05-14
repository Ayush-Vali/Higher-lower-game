# from game_data import data
# from art import logo, vs
# import random


# def Compare(r1, r2):
#     """It takes two random input number based on which two data to be compared are jotted down """
#     print(logo)
#     print(
#         f"Compare A: {data[r1]['name']}, {data[r1]['description']}, from {data[r1]['country']}"
#     )

#     if r2 == r1:
#         rguess = True
#         while rguess:
#             r2 = random.randint(0, 1)
#             if r2 != r1:
#                 print(vs)
#                 print(
#                     f"Against B: {data[r2]['name']}, {data[r2]['description']}, from {data[r2]['country']}"
#                 )

#                 rguess = False

#     else:
#         print(vs)
#         print(
#             f"Against B: {data[r2]['name']}, {data[r2]['description']}, from {data[r2]['country']}"
#         )


# #option  select and count
# def rightorwrong(A, B, sel):
#     """Choose from the two options and checks for if the guess was right or wrong and returns the score"""

#     global score
#     if sel == "A":
#         if A > B:
#             score = score + 1
#             print(f"You're right, current score is: {score}")
#             return score + 1
#         else:
#             print(f"You loose, your final score is: {score}")
#             return False

#     else:
#         if A < B:
#             score = score + 1
#             print(f"You're right, current score is: {score}")
#             return score + 1
#         else:
#             print(f"You loose, your final score is: {score}")
#             return False


# def game():
#     """Repeat the iteration until the player selects right option,increasing score"""
#     stop = True
#     while stop:
#         ra = random.randint(0, 49)
#         rb = random.randint(0, 49)

#         Compare(ra, rb)
#         select = input("Who has more followers, A or B:")
#         A = data[ra]['follower_count']
#         B = data[rb]['follower_count']

#         stop = rightorwrong(A, B, select)


# gam = True
# while gam:
#     c = input("Do you want to play y or n:")
#     if c == "y":

#         score = 0
#         game()

#     else:
#         gam = False
# """Selects """


# # import instructers

import improv