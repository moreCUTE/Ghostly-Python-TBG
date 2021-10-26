import random
def Monsters():
    num = random.randrange (1,100)
    if num <= 30:
        print("Vampire apeared and suk ye blood")
    elif num <= 50:
        print("Mummy spawns")
    else:
        print("yes nothing there")
    
room = 1
print("Welcome to my basement!")
while True:
    if room == 1:
        print("You are in room 1. You can go 'n'orht or 'e'ast")
        choice = input()
        if choice ==  'e':
            room = 2
        elif choice == 'n':
            room = 4
        else:
            print("thats a wall")
    if room == 2:
        print("You are in room 2. You can go 'n'orth or 'w'est")
        Monsters()
        choice = input()
        if choice == 'w':
            room = 1
        elif choice == 'n':
            room = 3
        else:
            print("thats a wall")
    if room == 3:
         print("You are in room 3. you can go 'w'est or 's'outh")
         choice = input()
         if choice == 'w':
             room = 4
         elif choice == 's':
              room = 2
         else:
            print("thats a wall")
    if room == 4:
         print("You are in room 4. you can go 'e'ast or 's'outh")
         choice = input()
         if choice == 'w':
              room = 5
         elif choice == 's':
              room = 1
         else:
             print("thats a wall")
    if room == 5:
         print("You are in room 5. you can go 'e'ast")
         Monsters()
         choice = input()
         if choice == 'e':
           room = 4
         else:
          print("thats a wall")
     
    
          
