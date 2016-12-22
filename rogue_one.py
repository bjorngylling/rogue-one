#!/usr/bin/env python3

import tdl
import esper

from rogueone.app import RogueOneApp

SCREEN_WIDTH, SCREEN_HEIGHT = 80, 50
LIMIT_FPS = 20

tdl.set_font('terminal12x12_gs_ro.png')
console = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, 'rogue-one')
tdl.set_fps(LIMIT_FPS)

RogueOneApp(console).run()
