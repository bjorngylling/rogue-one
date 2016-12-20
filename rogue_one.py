#!/usr/bin/env python3

import tdl

SCREEN_WIDTH, SCREEN_HEIGHT = 80, 50
LIMIT_FPS = 20

tdl.set_font('terminal12x12_gs_ro.png')
console = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, 'rogue-one')
tdl.set_fps(LIMIT_FPS)

while True:
    console.clear()
    console.drawStr(1, 2, 'rogue-one')
    tdl.flush()

    for event in tdl.event.get():
        if event.type == 'QUIT':
            raise SystemExit('The window has been closed.')
