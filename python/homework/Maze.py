
def right():
    turn_left()
    turn_left()
    turn_left()
    move()
    
    
    

        
while front_is_clear():
    move()
turn_left()
    
while not at_goal(): 
    if front_is_clear() and wall_on_right():
        move()
    elif right_is_clear():
        right()
    else:
        turn_left()
        
        
        
        

        
        
            
        
        
                   
            
                                 
                    
            
    
    
            
    
    
    

    

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
