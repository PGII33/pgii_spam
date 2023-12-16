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
        temp = Image.new(mode, size)
        temp.load()
        self.size = temp.size
        self.mode = temp.mode
        self.im = temp.im
        self.info = temp.info.copy()
        return temp

    def __open_image(self, path:str)->Image:
        temp = Image.open(os.getcwd() + path)
        temp.load()
        self.size = temp.size
        self.mode = temp.mode
        self.im = temp.im
        self.info = temp.info.copy()
        return temp

    def monochrome(self, better_img:bool = False)->Image:
        ''' Return the image in grey variations, turn better_img on to have coef '''
        img2= Image.new(mode = 'L', size=(self.width, self.height))
        for i in range(self.width):
            for j in range(self.height):
                if better_img:
                    sum_pixel = 0.2126*self.getpixel((i,j))[0]+0.7152*self.getpixel((i,j))[1]+0.0722*self.getpixel((i,j))[2]
                else:
                    sum_pixel = self.getpixel((i,j))[0] + self.getpixel((i,j))[1] + self.getpixel((i,j))[2]
                sum_pixel //= 3
                sum_pixel = int(sum_pixel)
                img2.putpixel((i, j), sum_pixel)
        return img2

    def show(self, title:str|None = None):
        ''' Show the Image '''
        self.img.show(title)

a = PgiiImage("\\pgii_utilities\\python\\toon.png")
print(a.size, a.mode, a.width, a.height)