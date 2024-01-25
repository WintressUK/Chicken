import time
alive = True

#introduction to the game
def intro(): 
    global alive
    #define the options
    print("LITTLE CHICKEN: THE OFFICIAL GAME")
    time.sleep(2)
    print("You are an adventurer in a small village. A little chicken appears before you. It begins to chirp. What do you do?")
    time.sleep(2)
    
    #options
    print("1. Walk away and ignore it - you have things to do")
    print("2. Pick it up and stroke its cute little chicken head")
    print("3. Feed it seed")
    
    #get user input
    user_choice = input("Please enter your choice: ")

    #process the choice
    if user_choice == "1":
        time.sleep(2)
        print("You instantly die. How could you ignore such a cute and adorable little chicken. You are an evil monster. GAME OVER")
        alive = False
    elif user_choice == "2":
        time.sleep(2)
        print("You pick up the little chicken and stroke its cute little head. However, the chicken gods are angry that you dared to pick up a little chicken without feeding it seed. You instantly die. GAME OVER")
        alive = False
    elif user_choice == "3":
        time.sleep(2)
        print("You decide to feed the little chicken some seed. It loves you! It is now your little chicken")
    else:
        time.sleep(2)
        print("The little chicken turns into a shadow monster and consumes you whole. This is your punishment for fucking with my program. GAME OVER")
        alive = False
        
def chapter1():
    global alive
    time.sleep(2)
    print("CHAPTER 1")
    time.sleep(2)
    print("The little chicken jumps around happily. It is soooo happy because you gave it seed.")
    time.sleep(2)
    print("What will you name the little chicken?")
    time.sleep(2)
    name = input("Please enter a name: ")
    time.sleep(2)
    print("The little chicken", name, "loves your choice!!")
    time.sleep(2)
    print(name, "begins to chirp once again. What do you do?")
    time.sleep(2)
    
    #options
    print("1. Feed it additional seed. It wanted that last time")
    print("2. Begin to take it on walkies. Little chickens need walkies every day.")
    print("3. Wrap it up in a blankie. Maybe the little chicken is cold.")
    
    #get user input
    user_choice = input("Please enter your choice: ")
    
     #process the choice
    if user_choice == "1":
        time.sleep(2)
        print("Your little chicken is too full!! It is now uncomfy and sad and has a tummyache. It runs away to find a better owner who doesn't hate it. GAME OVER")
        alive = False
    elif user_choice == "2":
        time.sleep(2)
        print("You cradle the little chicken in your hands and head out. The little chicken is so happy! It loves walkies")
    elif user_choice == "3":
        time.sleep(2)
        print("The little chicken is overstimulated now D: It runs away to find a better owner who doesn't hate it. GAME OVER")
        alive = False
    else:
        time.sleep(2)
        print("The little chicken turns into your Year 10 English teacher and talks about Shakespeare for 100 years. You die of boredom after 14 years. This is your punishment for fucking with my program. GAME OVER")
        alive = False
    return name
        
def chapter2(name):
    global alive
    time.sleep(2)
    print("CHAPTER 2")
    time.sleep(2)
    print("You and", name, "head out on a walkies adventure!")
    time.sleep(2)
    print("Where would you like to take your new little chicken?")
    time.sleep(2)
    
    #options
    print("1. The city centre! There are a lot of seed shops there, and your little chicken could get some cute accessories.")
    print("2. The beach! Little chickens love playing in the sand and building cute sandcastles.")
    print("3. The nearby forest! Your little chicken would love to see all the pretty flowers.")
    
    #get user input
    user_choice = input("Please enter your choice: ")
    
     #process the choice
    if user_choice == "1":
        time.sleep(2)
        print("You take your little chicken to a Christmas market in the nearby city. The little chicken is so happy! It chirps and everyone at the market loves it so much that they give it free accessories and Christmas seed (roasted nuts).")
    elif user_choice == "2":
        time.sleep(2)
        print("You head out towards the beach. On your way there, you encounter a horde of evil zombies on the cliffs. Little chickens are soooo scared of zombies. The little chicken gods save the little chicken, and you are left to be devoured by zombies. GAME OVER")
        alive = False
    elif user_choice == "3":
        time.sleep(2)
        print("You and the little chicken arrive at the forest. However, banana cat and happy happy happy cat are already there. The little chicken loves them and runs away from you to join their party instead. GAME OVER")
        alive = False
    else:
        time.sleep(2)
        print("You are now a computer science student for all eternity. This is your punishment for fucking with my program. GAME OVER")
        alive = False
      
def play():
    intro()
    if alive == True:
        name = chapter1()
        if alive == True:
            chapter2(name)
            if alive == True:
                print("You and the little chicken have survived the game!! (for now). Please eat seed in real life as a reward.")
            else:
                print("u failed at the last round how depressing")

play()

#the chicken void
print*("Your Little Chicken Loves The Chicken Void")

print("you are eeeevil")