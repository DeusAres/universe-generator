from funPIL import df
import numpy as np
from pathlib import Path
import random
from PIL import Image


def rmf(image):
    if random.randint(0,1):
        image = df.rotate(image, random.randint(1, 4)*90)[0]
    if random.randint(0,1):
        image = df.mirror(image)
    if random.randint(0,1):
        image = df.flip(image)

    return image

def shiftColors(image):
    imgNP = np.array(image)
    shift = random.randint(30, 270)

    colors = np.unique(imgNP[imgNP[:,:,3]==255], axis=0).tolist()
    temp = [df.rgbToHsl(*each[:-1]) for each in colors]
    shiftedColors = [df.addColor(each, [shift, 0, 0]) for each in temp]
    shiftedColors = [df.hslToRgb(*each) for each in shiftedColors]
    
    image = df.replaceColor(image, colors, shiftedColors)

    return image


def makePlanet(planet, overlay, sat, xMult):
    
    xMult = xMult//max(df.openImage(planet)[0].size)

    def a(file):
        file = df.openImage(file)[0].convert('RGBA')
        
        file = shiftColors(file)
        file = rmf(file)
        file = df.resizeToFit(file, max(file.size)*xMult, False, Image.NEAREST)[0]

        return file
    
    planet = a(planet)
    overlay = a(overlay)
    sat = [a(each) for each in sat]

    planet = df.cropToRealSize(planet)[0]
    w, h = planet.size
    planet = df.expand(planet, w*3, h*3)[0]

    planet = df.pasteItem(planet, overlay, *df.centerItem(planet, overlay))

    for each in sat:
        x, y = random.randint(w, w*2), random.randint(h, h*2)
        planet = df.pasteItem(planet, each, x, y)

    return df.cropToRealSize(planet)[0]

def makeAlone(alone):
    alone = df.openImage(alone)[0].convert('RGBA')
    alone = shiftColors(alone)
    alone = rmf(alone)
    alone = df.cropToRealSize(alone)[0]

    return alone

def listDir(path):
    files = path.glob('**/*')
    return [str(each) for each in files if each.is_file()]   

def main(squares, W, H):
    mainPath = Path(__file__).parents[0]
    folders = mainPath / "images"
    
    types = "ALONE", "PLANETS", "OVERLAY", "SAT", "TILES"

    folders = [listDir(folders / each) for each in types]

    canvas = df.backgroundPNG(W, H)[0]

    tile = df.openImage(random.choice(folders[4]))[0].convert('RGBA')
    tile = df.resizeToFit(tile, min(canvas.size)//3, False, Image.NEAREST)[0]
    for x in range(0, W+tile.width, tile.width):
        for y in range(0, H+tile.height, tile.height):
            if random.randint(0, 1): tile = df.mirror(tile)
            if random.randint(0, 1): tile = df.flip(tile)
            canvas = df.pasteItem(canvas, tile, x, y)

    for each in squares:

        w, h = [z2-z1 for z2, z1 in zip(each.x2y2, each.x1y1)]

        if random.randint(0,1):
            # PLANETS
            image = makePlanet(*[random.choice(each) for each in folders[1:3]], random.sample(folders[3], random.randint(1, 2)), max(w, h))
        else:
            # ALONE
            image = makeAlone(random.choice(folders[0]))
            image = df.resizeToFit(image, max(w, h), False, Image.NEAREST)[0]

        x, y = each.center
        x, y = x-image.width//2, y-image.height//2
        image = df.pasteItem(canvas, image, x, y)
        
    return canvas


