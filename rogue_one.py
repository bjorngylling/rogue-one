#!/usr/bin/env python3

import tdl

#actual size of the window
SCREEN_WIDTH, SCREEN_HEIGHT = 80, 50
 
LIMIT_FPS = 20  #20 frames-per-second maximum
 
#############################################
# Initialization & Main Loop
#############################################
 
tdl.set_font('terminal12x12_gs_ro.png')
console = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, 'rogue-one')
tdl.set_fps(LIMIT_FPS)
 
playerx = SCREEN_WIDTH//2
playery = SCREEN_HEIGHT//2
 
while True:
    console.clear()

    console.drawStr(1, 2, 'rogue-one')
 
    tdl.flush()

    # Handle events by iterating over the values returned by tdl.event.get
    for event in tdl.event.get():
        # Check if this is a 'QUIT' event
        if event.type == 'QUIT':
            # Later we may want to save the game or confirm if the user really
            # wants to quit but for now we break out of the loop by raising a
            # SystemExit exception.
            # The optional string parameter will be printed out on the
            # terminal after the script exits.
            raise SystemExit('The window has been closed.')
