def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdles():
    if right_is_clear():
        turn_right()
    if wall_in_front(): 
        turn_left()
    if front_is_clear():
        move()    

while not at_goal(): 
    hurdles()