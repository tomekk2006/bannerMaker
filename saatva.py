from PIL import Image, ImageChops, ImageColor
from constants import *
import math
import copy
from queue import Queue
from threading import Thread
#texture class
class Texture:
    image:Image.Image
    textureCode:str
    colorCode:str
    def __init__(self, textureCode:str, colorCode:str):
        self.textureCode = textureCode
        self.colorCode = colorCode
        self.image = tint(getTextureByCode(textureCode), getColorByCode(colorCode))
    def getCode(self):
        return self.colorCode+self.textureCode
    def convert(self, format:str):
        self.image = self.image.convert(format)
        return self

#banner class
class Banner:
    image:Image.Image
    textureCodes:list[str]
    colorCodes:list[str]
    def __init__(self):
        self.image = Image.new("RGBA",(20,40))
        self.textureCodes = []
        self.colorCodes = []
    def getCode(self):
        code = ""
        for i in range(len(self.textureCodes)):
            code += self.colorCodes[i] + self.textureCodes[i]
        return code
    def addTexture(self, texture:Texture):
        self.image.alpha_composite(texture.image)
        self.colorCodes.append(texture.colorCode)
        self.textureCodes.append(texture.textureCode)
        return self
        
        
class Score:
    banner:Banner
    score:float
    def __init__(self, banner:Banner, score:float):
        self.banner = banner
        self.score = score
    def __str__(self):
        return str(self.score)

# prints array as an ordered list
def orderedPrint(array):
    for x in range(len(array)):
        print(f"{x}: {array[x]}")

# tint image
def tint(image:Image.Image, color:ImageColor) -> Image.Image:
    if image.mode == "RGBA":
        r, g, b, a = image.split()
        r = r.point(lambda x: x*(color[0]/255))
        g = g.point(lambda x: x*(color[1]/255))
        b = b.point(lambda x: x*(color[2]/255))
        return Image.merge("RGBA", (r,g,b,a))
    elif image.mode == "RGB":
        r, g, b = image.split()
        r = r.point(lambda x: x*(color[0]/255))
        g = g.point(lambda x: x*(color[1]/255))
        b = b.point(lambda x: x*(color[2]/255))
        return Image.merge("RGB", (r,g,b))
    else:
        return image

# sums up all amplitudes of each color
def calculateScore(banner:Banner, target:Image.Image):
    image = ImageChops.difference(banner.image, target)
    
    data = list(image.getdata())
    sum = 0
    for r, g, b, a in list(data):
        sum += math.sqrt(r**2+g**2+b**2)
    return sum

# sorts scores
def sortScores(scores:list[Score], max=0, reverse=False):
    scores.sort(key=(lambda x: x.score), reverse=reverse)
    if max != 0:
        return scores[:max]
    else:
        return scores
    
# create banners with 16 coloured bases
def getAllBases() -> list[Banner]:
    banners:list[Banner]=[]
    colorCodes = getColorCodes()
    for color in colorCodes:
        banner = Banner()
        banner.addTexture(Texture("a",color).convert("RGBA"))
        
        banners.append(banner)
    return banners

# get all combonation of a single score
def scoreCombos(score:Score, target):
    textureCodes = getLegacyTextureCodes()[1:]
    colorCodes = getColorCodes()
    scores = [score]
    for textureCode in textureCodes:
        for colorCode in colorCodes:
            banner = copy.deepcopy(score.banner)
            texture = Texture(textureCode, colorCode)
            banner.addTexture(texture)    
            scores.append(
                Score(banner,calculateScore(banner, target)))
    return scores

def threadScoreCombos(score:Score, target, queue:Queue, output:list):
    textureCodes = getLegacyTextureCodes()[1:]
    colorCodes = getColorCodes()
    scores = [score]
    for textureCode in textureCodes:
        for colorCode in colorCodes:
            banner = copy.deepcopy(score.banner)
            texture = Texture(textureCode, colorCode)
            banner.addTexture(texture)    
            scores.append(
                Score(banner,calculateScore(banner, target)))
    output += scores
    task = queue.get()
    print(f"✅ thread {task}")
    queue.task_done()

# save all scores from a list
def save(scores:list[Score]):
    for i in range(len(scores)):
        scores[i].banner.image.save(f"results/{i}_{scores[i].banner.getCode()}.png")                

# score the list        
def scoreList(banners:list[Banner], target) -> list[Score]:
    scores = []
    for banner in banners:
        score = calculateScore(banner,target)
        scores.append(Score(banner,score))
    return scores

def scoreComboList(scores:list[Score], target) -> list[Score]:
    output = []
    queue = Queue()
    for i in range(len(scores)):
        print(f"🔄️ thread {i}")
        Thread(target=threadScoreCombos, args=(scores[i], target, queue, output), daemon=True).start()
        queue.put(i)
    queue.join()
    return output