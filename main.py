import tkinter.dialog
import tkinter.filedialog
from PIL import Image
from constants import *
from saatva import *
import time
import tkinter
from tqdm import tqdm

if __name__ == '__main__':
    
    print("Banner Creator by tomekk06")
    input("Press enter to select an image to convert")
    resultPath = "results/result.png"
    target = tkinter.filedialog.askopenfilename()
    target = Image.open(target).convert("RGBA")
    if target.size != (20,40):
        target = target.resize((20,40))
        target.save('converted_target.png')
    maxScores = 8   # max 61
    iterations = 8 # max 8
    
    layerProgress = tqdm(total=iterations, desc="Progress", unit="layer")
    
    
    start = time.time()
    bases = getAllBases()
    scores = scoreList(bases, target)
    for x in range(iterations):
        layerProgress.update(1)
        scores = scoreComboList(scores, target)
        if x == 0:
            scores = [ score for score in scores if len(score.banner.getCode()) > 3 and score.banner.getCode()[0] != score.banner.getCode()[2]]
        else:
            scores = [ score for score in scores if len(score.banner.getCode()) > 3 and score.banner.getCode()[-1] != score.banner.getCode()[-3]]
        scores = sortScores(scores, maxScores)
    
    layerProgress.close()
    scores[0].banner.image.save('result.png')
    end = time.time()
    print(f"🏁 Finished in {end-start} seconds")
    print("Result saved as 'result.png'")
    print(f"Url: https://livzmc.net/banner/?={scores[0].banner.getCode()}")




