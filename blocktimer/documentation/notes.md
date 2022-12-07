# Timer

## Important

- clear and initialize the database  
`flask --app blocktimer init-db`
- start the app
`py -m flask --app blocktimer --debug run`
`$ py -m flask --app blocktimer --debug run --host=0.0.0.0`

## Log

- 20221005
  - updated timer with better visuals and m/s
  - next step - add pause / resume button

- 20221008
  - stuck on return statement in save route, timer.py lines 144/145, code is returning a memory address rather than the actual timer id - SOLVED - deb execute fetch one returns the first match as an object, need to use  `[0]` to get the actual value
  - [x] why does this not apply to the same in the auth function? line 53  

- 20220109
  - finish save and load functionality
  - I think the main functionality is all working, not I just need to change esthetics, check for errors, refactor, document
  - 18:48 I need to figure out the parse time block function to handle minutes and seconds together
  - 21:10 I have the parse time block function tested and working!  

- 20221010
  - need to check all functionality for various bugs
    - timer  
      - clearing when finished / using clear

- 20221011
  - timer working again
  - need to refactor timer route code

- 20221015
  - working on refactoring the app - timer code

- 20221022
  - [X] home button on top bar
  - css, clean up looks
  - [X] when making timer - site doesn't default to text entry

- 20221023
  - [X] work on aesthetics
  - ! bug when not entering s or m with time entry
  - ! bug can see other users timers listed when trying to load
  - [] test aesthetics on various device sizes
  - ! bug, if cleared cant enter
  - [X] change flash error formats
  - [] buttons all the same size
  - [] vertical align black box app

- 20221024
  - [] timer to home no longer shows title
    - need to save timer name as session param?
  - [] show timer name on actual timer screen
  - [] show start save / clear buttons on top, so scrolling isn't necessary
  - [] bug with "run 5" entry still works but should give error
  - [] need to limit time to 24hrs to prevent huge numbers
  - [] make the table scrollable so the buttons always show
  - [] round corners on top and bottom of table
  - [] deselect button on hover with touch screen
  - [] make clearer instructions
  - [] keep text with error on entry
  - [] parse min and sec also
  - [] !! save button is weird
  - [] !! save  / load functionality is very broken

## To Do

### Inbox

- [X] 20221005 create pause / start
- [X] 20221005 fix timer display
- [X] 20221008 save / load timers
  - [X] 20221008 login required
- [X] 20221008 fix parse function to handle both minutes and seconds
- [X] 20221008 overall esthetic enhancements
- [] 20221008 keep consistent naming conventions for variables, and parts of code
- [] 20221008 change all time representations to M:S
- [X] 20221008 default to text entry on index screen
- [] 20221008 show timer name on index once it has one
- [X] 20221009 handle errors in save / load routes
- [] 20221009 write tests
- [] 20221009 remove testing dependency on setting env app name
- [X] 20221009 build logout functionality
- [] 20221009 fix requiring double click when going home from the timer
- [] 20221009 add home button everywhere  
- [] 20221009 if arrived at login from @login_required send back to original page (save, etc.)
- [] 20221009 if login from @login_required it clears your current timer
- [X] 20221009 show list of upcoming blocks on timer page
- [] 20221009 handle parse_time_block with no name
- [] 20221010 default timezone not correct
- [X] 20221010 timer still showing brief negative between blocks
- [] 20221010 show complete screen when finished
- [] Bugs
  - [X] 20221010 clear does not actually clear the stored session timer
  - [x] pausing timer in middle of block and going back to the main screen does not resume properly
        - reason is because it does not pop the session
- [] 20221019 do not automatically start timer, must click start button
- [X] ! 20221019 load->start->home->clear doesn't clear
- [] 20221019 save screen needs a home button
- [] 20221022 text parse in entry to start timer
- [] 20221022 load when not logged in goes back to index and not load screen

### Working

### Complete

## Reference

- name: BLock Timer
  - a timer made up of blocks of varying time sizes
- goal: an app to easily make a quick timer using text parsing, no clicking needed
- a block consists of a name and a unit of time
  - the name can be any text, typically it should be a description of the activity.
  - the time can be any unit of time

## Project Structure

- /final
  - /blocktimer
    - entry.py
    - auth.py
    - db.py
    - timer.py
    - helpers.py
  - /templates
    - /auth
      - login.html
      - register.html
    - /blocktimer
      - index.html
      - load.html
      - save.html
      - timer.html
    - base.html
