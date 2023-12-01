import turtle as t
import numpy as np

def gamecheck(game):
    '''
    

    Parameters
    ----------
    game : NumPy Array
    
    Checks the current gamestate array to see if it matches a win condition

    '''
    
    #Finds the current positions of Black and converts them to a form we check
    gameBlack = game.copy()
    gameBlack[gameBlack == 1] = -1
    gameBlack[gameBlack == 0] = 1
    
    #Finds the current positions of Red and converts them to a form we check
    gameRed = game.copy()
    gameRed[gameRed == 0] = -1
    
    
    with open("C:\\Users\\Parker\\Documents\\Python Scripts\\teeko_win_conditions_formatted.txt") as winstates:
        
        for line in winstates.readlines():
            line = line.strip().split("],[")
            for i in range(5):
                line[i] = [int(j) for j in line[i].split(",")]
            
            statearray = np.array(line)
            
            if np.array_equal(gameBlack, statearray):
                return 1
            
            if np.array_equal(gameRed, statearray):
                return 2
    
    return 0

