import curses;
from random import randint
#setting up the window
curses.initscr()
# this means that y axes will load first and then x-axes will come
win= curses.newwin(20,60,0,0) 
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)  # -1

#snak and food
#for snake we are using a list 
snake= [{4,10}, {4,9},{4,8}]
food= {10,20}



# this will be the game logic
score = 0


ESC = 27
key = curses.KEY_RIGHT 

while key != ESC:
    win.addstr(0, 2, 'Score : ' + str(score) + ' ')  
    win.timeout(150 - (len(snake)) // 5 + len(snake) // 10 %120) # increase the speed
    
    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        keys = prev_key
    
    
    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

    # If snake crosses the boundaries, make it enter from the other side
    if snake[0][0] == 0: snake[0][0] = 18
    if snake[0][1] == 0: snake[0][1] = 58
    if snake[0][0] == 19: snake[0][0] = 1
    if snake[0][1] == 59: snake[0][1] = 1

    # Exit if snake crosses the boundaries (Uncomment to enable)
    #if snake[0][0] == 0 or snake[0][0] == 19 or snake[0][1] == 0 or snake[0][1] == 59: break



    #check if we hit the border

    if y == 0: break
    if y == 19: break
    if x == 0: break
    if x == 59: break

    # IF SNAKE RUNS over it self, then
    if snake[0] in snake[1: ]: break


    if snake[0] in food:
        score += 1
        food = ()
        while food == ():
            food = (randint(1,18), randint(1,58))
            if food in snake: 
                food = ()
        win.addch(food[0], food[1], '#')   
    else:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')

    win.addch(snake[0][0], snake[1][0], '*')   




curses.endwin()
print("Final Score = {score}")