from MapGeneration import BaseGenerator


class RandomRoomGenerator(BaseGenerator):
    """This class will generate a random room (square or rectangle for now)
    inside the provided map"""

    def __init__(self, bounds):
        self.bounds = bounds

    def run(self, map):
        return
