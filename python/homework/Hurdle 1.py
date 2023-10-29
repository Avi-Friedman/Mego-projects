def function_r():
    for i in range(2):
        move()
        turn_left()
        turn_left()
        turn_left()
        
def function_l():
    move()
    turn_left()
    
def function_game():
    for i in range (6):
        function_l()
        function_r()
        function_l()
        
function_game()
    

    

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
