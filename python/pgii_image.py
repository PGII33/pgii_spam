''' PGII coded this, it's all about Image, to understand how it works, and maybe to use it later'''
import os
from PIL import Image

class PgiiImage(Image.Image):
    ''' PGII Image class (using pillow)'''
    def __init__(self, path:str|None = None, mode:str = '1', size:tuple = (1,1)):
        super().__init__()
        self._size = size
        self._mode = mode
        self._path = path
        if path is None :
            self.img = self.__create_image(mode, size)
        else:
            self.img = self.__open_image(path)

    @property
    def width(self):
        return self.size[0]
    @property
    def height(self):
        return self.size[1]
    @property
    def size(self):
        return self._size
    @property
    def mode(self):
        return self._mode
    @size.setter
    def size(self, element):
        self._size = element
    @mode.setter
    def mode(self, element):
        self._mode = element

    def __create_image(self, mode:str, size:tuple)->Image:
        ''' Create the Image '''
        return Image.new(mode, size)

    def __open_image(self, path:str)->Image:
        temp = Image.open(os.getcwd() + path)
        self.size = temp.size
        self.mode = temp.mode
        return temp

    def show(self, title:str|None = None):
        ''' Show the Image '''
        self.img.show(title)

a = PgiiImage("\\pgii_utilities\\python\\toon.png")
print(a.size, a.mode, a.width, a.height)
