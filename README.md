# Python Documentation

## Classes

**[Settings](Settings.md)**: a class to represent the settings of the game 

**[Game](Game.md)**: a class to initialize the game's display 

**[Entity](Entity.md)**: Class to represent an entity 

**[Ball](Ball.md)**: Class to represent the ball ... Methods ------- update() - updates the ball's position restart() - resets the ball's position 

**[Player](Player.md)**: Class to represent the player ... Methods ------- update() - updates the player's position move() - moves the player move_left() - moves the player left move_right() - moves the player right update_score() - updates the player's score restart() - resets the player's position and score 


## Functions

### run_game


run the game   
This function is the main function of the game. It checks the python version, initializes pygame, initializes the display and runs the game loop. While the loop is running , it checks for events and updates the game. When the ball is lost to the bottom of the screen, the game is over and the end screen is displayed. The player can restart the game by pressing the space bar. 




### instantiate_game_entities



#### Parameters
name | description | default
--- | --- | ---
game |  | 





### create_sprite_group



#### Parameters
name | description | default
--- | --- | ---
ball |  | 
player |  | 





### display_running_game



#### Parameters
name | description | default
--- | --- | ---
game |  | 
player |  | 
sprite_group |  | 





### render_score_text



#### Parameters
name | description | default
--- | --- | ---
game |  | 
player |  | 





### show_end_screen



#### Parameters
name | description | default
--- | --- | ---
game |  | 
player |  | 





### render_end_screen_text



#### Parameters
name | description | default
--- | --- | ---
font |  | 
player |  | 





### blit_end_screen_text



#### Parameters
name | description | default
--- | --- | ---
game |  | 
end_screen_text |  | 





### check_for_restart



#### Parameters
name | description | default
--- | --- | ---
player |  | 
ball |  | 





### restart



#### Parameters
name | description | default
--- | --- | ---
player |  | 
ball |  | 





### update_entities



#### Parameters
name | description | default
--- | --- | ---
ball |  | 
player |  | 





### move_player



#### Parameters
name | description | default
--- | --- | ---
player |  | 





### check_for_quit



#### Parameters
name | description | default
--- | --- | ---
program_running |  | 





### detect_collision



#### Parameters
name | description | default
--- | --- | ---
ball |  | 
player |  | 





### detect_game_over



#### Parameters
name | description | default
--- | --- | ---
game |  | 
ball |  | 
game_running |  | 





### center_text_plus_x



#### Parameters
name | description | default
--- | --- | ---
game |  | 
text |  | 
x |  | 0





### check_python_version






