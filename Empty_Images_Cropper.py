from PIL import Image
from itertools import product
import os
import time
import random

DATA_FOLDER = "PieceImages"

Output_Folder = "CroppedImages"

PIECES = [
    "None"
]

POS = [
    "A1",
    "B1",
    "C1",
    "A2",
    "B2",
    "C2"
]

PICS_PER_POS = 15

crop_width = 170
crop_height = 300

Boxes = {
    "A1": (355, 30, 355 + crop_width, 10 + crop_height),
    "B1": (195, 30, 195 + crop_width, 10 + crop_height),
    "C1": (70, 30, 70 + crop_width, 10 + crop_height),
    "A2": (355, 128, 355 + crop_width, 128 + crop_height),
    "B2": (180, 128, 180 + crop_width, 128 + crop_height),
    "C2": (30, 128, 30 + crop_width, 128 + crop_height)
}



# Setup the data folder
if not os.path.isdir(Output_Folder):
    os.mkdir(Output_Folder)

for piece in PIECES:

    # Setup the piece folder
    if not os.path.isdir(os.path.join(Output_Folder, piece)):
        os.mkdir(os.path.join(Output_Folder, piece))

    for pos, value in product(POS, range(PICS_PER_POS)):
        im = Image.open(os.path.join(DATA_FOLDER, "B-Bishop", pos+str(value)+".jpg"))
        width, height = im.size

        random_box = random.choice(list(set(Boxes.keys()) - {pos}))

        cropped = im.crop(Boxes[random_box])
        outputpath = os.path.join(Output_Folder, piece, pos+str(value)+".jpg")

        cropped.save(outputpath)
