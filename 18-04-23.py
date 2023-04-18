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



####################################################


# Encapsulation
# Python doesn't have access modifier

class Foo:
    def __init__(self):
        self.public = 'this is public'
        self._protected = 'this is protected'
        self.__private = 'this is private'

    def public_method(self):
        self._protected_method()
        print(self.__private)
        return 'public method'

    def _protected_method(self):
        print('_protected_method')
        return 'protected method'

    def __private_method(self):
        print('&&&&__private_method')
        return 'private method'


f = Foo()
# print(f.public)
# print(f._protected)  # that's not right, shouldn't be possible - but names with underscore aren't imported
print(f.public_method())
print(f._Foo__private_method())  # name mangling --> name defacement
