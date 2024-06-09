from PIL import Image, ImageChops, ImageColor
from constants import *
from saatva import *



resultPath = "results/result.png"
target = Image.open("target.png").convert("RGBA")
maxScores = 8
iterations = 8 # max 8


if __name__ == '__main__':
    bases = getAllBases()
    scores = scoreList(bases, target)
    for x in range(iterations):
        print(f"Baking: {x+1}/{iterations}")
        scores = scoreComboList(scores, target)
        if x == 0:
            scores = [ score for score in scores if len(score.banner.getCode()) > 3 and score.banner.getCode()[0] != score.banner.getCode()[2]]
        else:
            scores = [ score for score in scores if len(score.banner.getCode()) > 3 and score.banner.getCode()[-1] != score.banner.getCode()[-3]]
        scores = sortScores(scores, maxScores)
    save(scores)
print("done.")




