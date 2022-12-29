# BlockTimer

## Video Demo: https://youtu.be/nm8vdnvmxMc

## Description

My app is a timer which allows for quick parsing of text-only inputs. The idea behind creating this timer was to allow the quick creation of multiple time blocks with differing names and lengths. Most online timers only allow repeated blocks of time and require a lot of clicking in order to set up a timer. This app allows for text-only entry to create a timer.

## Main Functionality

The main functionality of the BlockTimer app is as follows:

- parse a time block in the format of 'Activity Name' 'Activity Time'
- an activity time can be in seconds, minutes or minutes and seconds
  - ex: 30s, 30m, 30s30m
- when a time block is entered it is added to the timer, the app then defaults back to timer entry to allow for quick text entry of multiple blocks
- the timer can then be started
- the timer will show the name of the current block and all of the upcoming blocks
- the timer can be paused and resumed
- from the timer screen, you can go back to the main screen
- from the main screen, the timer can be cleared so a new one can be created
- all of this can be done without logging in
- the app also allows for registration, login and log out
- once registered users are able to save a timer under a name
- saved timers can be loaded to be used again, they are sorted by the date they were created

## Project Structure

I followed the flask tutorial structure to set up my project. The init.py file registers the app and all of the related blueprints. The entry.py handles the main app logic and routing. The helpers.py file contains the logic to parse the time entry blocks. This file required a lot of testing in order to ensure the logic works properly. It was easier to test and troubleshoot as a separate file. The auth.py file handles registration, login and logout as well as a login_required function which enforces a login requirement for the load and save routes. The db.py file handles the creation of the initial database creation and accessing the database when the app is running. Schema.sql stores the database schema parameters for creation. The static folder contains the styling CSS elements, bootstrap was used as a template for the styling. The blocktimer directory stores all of the HTML routes. All sub-pages are based on the base.html template which contains the main nav bar and overall app styling. Sub-pages include the index which is the main timer entry page, timer which is the main timer page and the save and load pages.

## Project Design

Design decisions for the project were centred around the visual representation of the app. I wanted to time block entry to be text only for quick text entry. All other buttons and functionality were kept to the bare minimum for simple quick navigation. The app needed to display easily on all devices and be easy to use. The main timer functionality also needed to be usable without requiring login.

## Future Development

Several feature ideas did not make it into the initial project and will hopefully be implemented in the future. The following are ideas for additional features:

- editing of saved timers
- deleting saved timers
- search saved timers
- sharing timers between users
- synching timers between users

## References Used

 1. flask tutorial: https://flask.palletsprojects.com/en/2.2.x/tutorial/
 2. bootstrap: https://getbootstrap.com/docs/5.3/getting-started/introduction/
 3. hiit timer: https://github.com/tecladocode/hiit-timer/tree/master/templates, https://www.youtube.com/watch?v=-cq--miq5NI&t=584s
 4. css table corners: https://unused-css.com/blog/css-rounded-table-corners/
 5. pause interval: https://www.delftstack.com/howto/javascript/javascript-pause-interval/
 6. app colors: https://www.happyhues.co/palettes/4