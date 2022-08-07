
import random
def findmultiple(x):
  lis=[]
  for i in range(2,x-1):
    if(x%i==0):
      lis.append(i)
  if(len(lis)<1):
    return 1
  else:
    res=random.choice(lis)
    return res

Total_lives=5
no=random.randint(1,100)
while(Total_lives>0):
  guess=int(input("Guess the Number in between 1-100:- "))
  if(no==guess):
    print("Wooho! you won the game with",Total_lives," lives")
    break
  elif(no<guess):
    print("You need to guess no lesser than ",guess)
    Total_lives-=1
    print("Total lives remaining= ",Total_lives)
  elif(no>guess):
    print("You need to guess no larger than ",guess)
    Total_lives-=1
    print("Total lives remaining= ",Total_lives)
  if(no%2==0):
    print("It is an even number")
  else:
    print("It is a prime number")
  if(findmultiple(no)==1):
    print("It is a prime no")
  else:
    print("Multiple of Number is ",findmultiple(no))

if(Total_lives<=0):
  print("Correct Answer is ",no)
  print("Sorry! You Lost the game")
  print("Better try next time")
  


