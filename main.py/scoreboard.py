# from turtle import Turtle
# FONT=("Courier", 24, "normal")
# ALIGNMENT="center"
# class ScoreBoard(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.highscore=0
#         self.penup()
#         self.color("white")
#         self.goto(0, 260)
#         self.hideturtle()
#         self.update_score()
#
#     def update_score(self):
#         self.clear()
#         file=open('data.txt')
#         contrxt=file.read()
#         self.write(f"Score: {self.score}    High Score:{contrxt}", align=ALIGNMENT, font=FONT)
#
#     def increase_score(self):
#         self.score += 1
#         self.update_score()
#
#     def high_score(self):
#         if self.score>self.highscore:
#             self.highscore=self.score
#             with open('data.txt','w') as file:
#                 gg=file.write(f'{self.highscore}')
#                 print(gg)
#
#
#             self.score=0
#             self.update_score()
#     # def high_score(self):
#     #     if self.score > self.highscore:
#     #         self.highscore = self.score
#     #         with open('data.txt', 'w') as file:
#     #             file.write(str(self.highscore) + '\n')
#     #
#     #         self.score = 0
#     #         self.update_score()
#num=int(input("Enter a number:"))
# temp=num
# rev=0
# while(num>0):
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
# if(temp==rev):
#     print("The number is palindrome!")
# else:
#     print("Not a palindrome!")
# # file=open('my_file.txt')
# # contrxt=file.read()
# # print(contrxt)
# # file.close()
#
# # with open('new_file.txt','w') as file:
# #     file.write('fvefr')
#     # print(contrxt)
#     # file.close()













num =int(input('enter number'))
temp =num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10

if (temp==rev):
    print('palindrome')
else:
    print('not')















