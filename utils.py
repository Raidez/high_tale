from PIL import Image

class Spritesheet():
    def __init__(self, uri = None, sprite_count = None, sprite_size = None):
        self.uvs = None
        self.image = None
        if uri:
            self._load_image(uri, sprite_count, sprite_size)
    
    def _load_image(self, uri, sprite_count = None, sprite_size = None):
        self.image = Image.open(uri)
        self.image = self.image.convert('RGBA')
        if sprite_count:
            self.sprite_count = sprite_count
            self.sprite_size = tuple(a // b for a, b in zip(self.image.size, sprite_count))
        if sprite_size:
            self.sprite_size = sprite_size
            self.sprite_count = tuple(a // b for a, b in zip(self.image.size, sprite_size))

        if not (sprite_count or sprite_size):
            raise ValueError("I can't guess only with image !")
    
    def __getattr__(self, name):
        return getattr(self.image, name)
    
    def __getitem__(self, key):
        if key > self.sprite_count or key < (0, 0):
            raise ValueError("Out of box")
        
        x, y = tuple(a * b for a, b in zip(self.sprite_size, key))
        w, h = tuple(a * (b + 1) for a, b in zip(self.sprite_size, key))
        box = (x, y, w, h)
        region = self.image.crop(box)
        return region
    
    @staticmethod
    def create(sprite_size, *, left, front, back, right, top, under):
        sp = Spritesheet()
        shape = {(0, 1): "left", (1, 1): "front", (2, 1): "back", (3, 1): "right", (1, 0): "top", (2, 0): "under"}

        im = Image.new('RGBA', (sprite_size[0] * 4, sprite_size[1] * 2))
        for position in shape:
            texture = locals()[shape[position]]
            x, y = position[0] * sprite_size[0], position[1] * sprite_size[1]
            box = (x, y, x + sprite_size[0], y + sprite_size[1])
            im.paste(texture, box)

        sp.image = im
        sp.uvs = (
            (1., .5), (.75, 0.), (1., 0.), # under
            (.5, 1.), (.25, .5), (.5, .5), # top
            (), (), (), # right
            (), (), (), # front
            (), (), (), # left
            (), (), (), # back
            (1., .5), (.75, .5), (1., 0.), # under
            (.5, 1.), (.5, .5), (.25, 1.), # top
            (), (), (), # right
            (), (), (), # front
            (), (), (), # left
            (), (), () # back
        )
        return sp
    
################################################################################

if __name__ == "__main__":
    # try to get furnace sprite with old way
    spritesheet = Image.open('assets/spritesheet_tiles.png')
    sprite_count = (9, 10)
    sprite_size = (128, 128)

    elem = (4, 4)
    x, y = tuple(size * count for size, count in zip(sprite_size, elem))
    w, h = tuple(size * (count + 1) for size, count in zip(sprite_size, elem))
    box = (x, y, w, h)
    region = spritesheet.crop(box)
    # region.show()

    # try with custom object
    sp = Spritesheet('assets/spritesheet_tiles.png', sprite_count = (9, 10), sprite_size = (128, 128))
    # sp[4, 4].show()

    # try creating texture with multiple image pasted inside
    im = Image.new('RGBA', (sp.sprite_size[0] * 1, sp.sprite_size[1]))
    pasted = [
        # sp[3, 4], # top
        sp[4, 4], # front
        # sp[3, 4], # left
        # sp[3, 4], # right
        # sp[3, 4], # ass
        # sp[3, 4]  # bottom
    ]

    for i, region in enumerate(pasted):
        w, h = region.size
        x, y = w * i, h * 0
        box = (x, y, x + w, y + h)
        im.paste(region, box)
    
    # im.show()
    # im.save('assets/furnace_front.png')

    # try to calculate UV from png file
    # im = Image.open('assets/cube_uv.png')
    # im = im.convert('RGBA')
    # founds = dict()
    # for x in range(1, im.size[0]):
    #     for y in range(1, im.size[1]):
    #         rgb = im.getpixel((x, y))
    #         if rgb in founds:
    #             founds[rgb] += 1
    #         else:
    #             founds[rgb] = 1
    
    # print(founds)

    a = sp[3, 4]
    im = Spritesheet.create((128, 128), front=sp[4, 4], top=a, back=a, left=a, right=a, under=a)
    # im.save('assets/furnace.png')
