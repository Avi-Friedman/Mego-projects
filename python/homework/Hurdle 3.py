
def right_1():
    turn_left()
    turn_left()
    turn_left()
    move()
    
def right():    
    for i in range (2):
        right_1()
        
def left():
    turn_left()
    move()
    
    
while not at_goal():
    if front_is_clear():
        move()
    else:
        left()
        right()
        turn_left()
        
    
            
    
    
    

    

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
