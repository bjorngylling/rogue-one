
class Rect(object):
    def __init__(self, pos, w, h):
        self.x1, self.y1 = pos
        self.x2 = self.x1 + w
        self.y2 = self.y1 + h
        self.w = w
        self.h = h

    def __repr__(self):
        return "<Rect x1:%s y1:%s x2:%s y2:%s w:%s h:%s>" % (self.x1,
                                                             self.x2,
                                                             self.y1,
                                                             self.y2,
                                                             self.w,
                                                             self.h)

    def center(self):
        center_x = (self.x1 + self.x2) / 2
        center_y = (self.y1 + self.y2) / 2
        return (center_x, center_y)

    def intersect(self, other):
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)

    def setSecondPos(self, pos):
        self.x2, self.y2 = pos
        self.w = self.x2 - self.x1
        self.h = self.y2 - self.y1
