"""
Tool for Cropping photos
"""

from PIL import Image
from itertools import product
import os
import time

DATA_FOLDER = "PieceImages"
Output_Folder = "CroppedImages"

# Names of the pieces
PIECES = [
    color+"-"+piece for color in "BW" for piece in ["King", "Queen", "Rook", "Bishop", "Knight", "Pawn"]
]
PIECES.append("None")

# Names of the Squares
POS = [
    letter+str(number) for letter in ['C', 'D', 'E', 'F', 'G'] for number in [2, 3, 4, 5]
]

# How many images at each position
PICS_PER_POS = 3

# Rough estimates of iomage size
crop_width = 128
crop_height = 175

# The boxes for each square we are looking at
Boxes = {
    "C2": (64, 185, 64+123, 185+184),
    "C3": (84, 121, 84+114, 121+173),
    "C4": (102, 61, 102+106, 61+170),
    "C5": (117, 22, 117+99, 22+153),

    "D2": (156, 172, 156+127, 172+195),
    "D3": (175, 120, 175+114, 120+179),
    "D4": (186, 67, 186+107, 67+167),
    "D5": (194, 23, 194 + 103, 23+156),

    "E2": (261, 197, 261+116, 197+170),
    "E3": (268, 133, 268+103, 133+162),
    "E4": (269, 69, 269+100, 69+162),
    "E5": (270, 21, 270+100, 21+152),

    "F2": (354, 191, 354+122, 191+173),
    "F3": (354, 132, 354+109, 132+165),
    "F4": (356, 72, 356+100, 72+158),
    "F5": (349, 25, 349+98, 25+160),

    "G2": (448, 188, 448+133, 188+190),
    "G3": (443, 119, 443+110, 119+181),
    "G4": (433, 71, 433+104, 71+158),
    "G5": (429, 24, 429+91, 24+152),
}

# Setup the data folder
if not os.path.isdir(Output_Folder):
    os.mkdir(Output_Folder)

# Iterate over all pieces
for piece in PIECES:

    # Setup the piece folder
    if not os.path.isdir(os.path.join(Output_Folder, piece)):
        os.mkdir(os.path.join(Output_Folder, piece))

    input_directory = os.path.join(DATA_FOLDER, piece)

    for filename in os.listdir(input_directory):

        # Filtering just the images from day2 of image taking
        if "_day2.jpg" not in filename:
            continue
        # Build image path
        im_path = os.path.join(input_directory, filename)

        # open image
        im = Image.open(im_path)
        width, height = im.size

        # position
        pos = filename[:2]

        cropped = im.crop(Boxes[pos])
        # cropped.show()

        outputpath = os.path.join(Output_Folder, piece, filename)

        cropped.save(outputpath)

        im.close()

    # # Do PICS_PER_POS photos per position
    # for pos, value in product(POS, range(PICS_PER_POS)):

    #     im = Image.open(os.path.join(DATA_FOLDER, piece, pos+str(value)+".jpg"))
    #     width, height = im.size

    #     cropped = im.crop(Boxes[pos])
    #     outputpath = os.path.join(Output_Folder, piece, pos+str(value)+".jpg")

    #     cropped.save(outputpath)
