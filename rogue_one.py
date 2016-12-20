#!/usr/bin/env python3

import tdl
import esper

from rogue_one import components
from rogue_one import processors

SCREEN_WIDTH, SCREEN_HEIGHT = 80, 50
LIMIT_FPS = 20

tdl.set_font('terminal12x12_gs_ro.png')
console = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, 'rogue-one')
tdl.set_fps(LIMIT_FPS)

world = esper.World()
player = world.create_entity(
    components.Position(1, 1),
    components.Renderable("@"))

world.add_processor(processors.RenderProcessor(console))

while True:
    world.process()
    tdl.flush()

    for event in tdl.event.get():
        if event.type == 'QUIT':
            raise SystemExit('The window has been closed.')
