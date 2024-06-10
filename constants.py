from PIL import Image, ImageColor

_textures = [
    ["banners/base.png","a"],
    ["banners/border.png","c"],
    ["banners/bricks.png","e"],
    ["banners/circle.png","t"],
    ["banners/creeper.png","k"],
    ["banners/cross.png","j"],
    ["banners/curly_border.png","i"],
    ["banners/diagonal_left.png","r"],
    ["banners/diagonal_right.png","J"],
    ["banners/diagonal_up_left.png","I"],
    ["banners/diagonal_up_right.png","x"],
    ["banners/flower.png","o"],
    ["banners/globe.png",None],
    ["banners/gradient_up.png","p"],
    ["banners/gradient.png","K"],
    ["banners/half_horizontal_bottom.png","L"],
    ["banners/half_horizontal.png","q"],
    ["banners/half_vertical_right.png","M"],
    ["banners/half_vertical.png","H"],
    ["banners/mojang.png",None], # not available for optifine (n)
    ["banners/piglin.png",None],
    ["banners/rhombus.png","v"],
    ["banners/skull.png","A"],
    ["banners/small_stripes.png","B"],
    ["banners/square_bottom_left.png","b"],
    ["banners/square_bottom_right.png","d"],
    ["banners/square_top_left.png","C"],
    ["banners/square_top_right.png","D"],
    ["banners/straight_cross.png","z"],
    ["banners/stripe_bottom.png","f"],
    ["banners/stripe_center.png","l"],
    ["banners/stripe_downleft.png","m"],
    ["banners/stripe_downright.png","n"],
    ["banners/stripe_left.png","s"],
    ["banners/stripe_middle.png","w"],
    ["banners/stripe_right.png","y"],
    ["banners/stripe_top.png","E"],
    ["banners/triangle_bottom.png","g"],
    ["banners/triangle_top.png","F"],
    ["banners/triangles_bottom.png","h"],
    ["banners/triangles_top.png","G"]
]
_colors = [
    ["#191919","black","a"],
    ["#993333","red","b"],
    ["#5E7C16","green","c"],
    ["#664C33","brown","d"],
    ["#334CB2","blue","e"],
    ["#7F3FB2","purple","f"],
    ["#4C7F99","cyan","g"],
    ["#999999","light_gray","h"],
    ["#4C4C4C","gray","i"],
    ["#F27FA5","pink","j"],
    ["#7FCC19","lime","k"],
    ["#E5E533","yellow","l"],
    ["#6699D8","light_blue","m"],
    ["#B24CD8","magenta","n"],
    ["#D87F33","orange","o"],
    ["#FFFFFF","white","p"],
]
class ColorNames:
    black = "black"
    red = "red"
    green = "green"
    brown = "brown"
    blue = "blue"
    purple = "purple"
    cyan = "cyan"
    light_gray = "light_gray"
    gray = "gray"
    pink = "pink"
    lime = "lime"
    yellow = "yellow"
    light_blue = "light_blue"
    magenta = "magenta"
    orange = "orange"
    white = "white"

def getTextures() -> list[Image.Image]:
    textures = [ Image.open(x[0]) for x in _textures ]
    return textures

def getLegacyTextures() -> list[Image.Image]:
    textures = [ Image.open(x[0]) for x in _textures if x[1] != None ]
    return textures

def getTextureCodes() -> list[str]:
    codes = [ x[1] for x in _textures ]
    return codes

def getLegacyTextureCodes() -> list[str]: 
    codes = [ x[1] for x in _textures if x[1] != None ]
    return codes

def getTextureCodeByPath(path:str):
    for texture in _textures:
        if texture[0] == path:
            return texture[1]

def getTextureByCode(code:str) -> Image.Image:
    for texture in _textures:
        if texture[1] == code:
            return Image.open(texture[0])

def getColors() -> list[tuple]:
    colors = [ ImageColor.getrgb(x[0]) for x in _colors ]
    return colors

def getColorCodes() -> list[str]:
    colors = [ x[2] for x in _colors ]
    return colors

def getColorByName(name:str):
    for color in _colors:
        if color[1] == name:
            return ImageColor.getrgb(color[0])

def getColorCodeByName(name:str):
    for color in _colors:
        if color[1] == name:
            return color[2]

def getColorByCode(code:str):
    for color in _colors:
        if color[2] == code:
            return ImageColor.getrgb(color[0])