# 1 or 2 underlines are "private / protected"

class Pen:
    def __init__(self, color='blue', color_cap='blue') -> None:
        self._color = color
        self._color_pen_cap = color_cap

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value


pen = Pen()
# setter
pen.color = 'pink'
# getter
print(pen.color)
