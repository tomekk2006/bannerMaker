from PIL import Image, ImageChops, ImageColor
from constants import *
from saatva import *



resultPath = "results/result.png"
target = Image.open("target.png").convert("RGBA")
maxScores = 24
iterations = 6


if __name__ == '__main__':
    bases = getAllBases()
    scores = scoreList(bases, target)
    for x in range(iterations):
        print(f"Baking: {x+1}/{iterations}")
        scores = scoreComboList(scores, target)
        scores = sortScores(scores, maxScores)
    save(scores)
print("done.")




