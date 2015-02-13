__author__ = 'raj'


class Vector:
    def __init__(self, _vid, _vector):
        self.vid = _vid
        self.co_ords = _vector

    def __hash__(self):
        return self.vid
