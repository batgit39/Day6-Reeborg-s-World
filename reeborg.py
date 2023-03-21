# this will not work in python go to this url to check the code : https://www.reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def move_right():
    turn_left()
    turn_left()
    turn_left()
    move()

  
    
while not at_goal():
    while front_is_clear() and right_is_clear():
        move()
    if right_is_clear():
        move_right()                    
    elif front_is_clear():
        move()
    else:
        turn_left()
