print("Welcome to the Star Game")
name=input("Name:")                                   #to input name
print(f"{name} ,you will have 21 stars and you will play with the computer \nOne can choose 1 or 2 or 3 or 4 stars in one go\nThe one picking the last star loses")
print(f"Are you ready {name}")
ready=input("Yes/No:")
while ready.lower()=="yes":                           #To check if the user wants to play again or is he ready to play
  for i in range(0,21):                               #To print the 21 stars
    print("*", end="")
  tstars=21                                           #a variable that keeps track of the total number of stars remaining after computer and users turn
  while tstars !=1:                                   #To continue the game until the total stars is not equal to 1, and the user loses
    print("\nYour turn")
    print("How many stars between 1 to 4 do you want to pick")
    user_stars=int(input("Stars:"))                   #To input the stars selected by users
    if stars>4:                                       #To display an error message if the number of stars exceeds 4
      print("Error pls pick stars between 1 to 4")
    else:
      tstars=tstars-user_stars                         #tstars as an accumulator and subtracts the number of stars picked by the user from the stars remn
      print("stars remaning are {tstars}:")
      for i in range(0,tstars):                        #to print the stars left after user has picked the choice     
        print("*", end="")
      print("\nComputer's turn")
      print(f"Computer picks {5-stars} stars")
      computer_stars=5-stars                           #The computer picks 5-user's stars so that 5*4 is 20 
      tstars=tstars-computer_stars                     #total stars remaining after computer makes the choice
      print(f"stars remaining are {tstars}:")
      for i in range (0,tstars):                       #to print the stars left after user has picked the choice 
        print("*", end="")

  print("\nHey, You have just lost the game to a bot, you loser")
  print("Do you want to continue?")
  ready=input("Yes/No:")                               #to store if the user wants to continue
else:
  print("Bye,Bye then Good for you")