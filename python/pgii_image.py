''' PGII coded this, it's all about Image, to understand how it works, and maybe to use it later'''
from PIL import Image

class PgiiImage(Image.Image):
    ''' PGII Image class (using pillow)'''
    def __init__(self, mode:str = '1', size:tuple = (1,1)):
        super().__init__()
        self.img = self.__create_image(mode, size)
        self._size = size
        self._mode = mode

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

    def __create_image(self, mode:str, size:tuple):
        ''' Create the Image '''
        return Image.new(mode, size)

    def show(self, title:str|None = None):
        ''' Show the Image '''
        self.img.show(title)

a = PgiiImage("1", (100, 100))
print(a.mode)
