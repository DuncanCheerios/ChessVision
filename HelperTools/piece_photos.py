"""
Simple Program to prompt me to take photos of chess pieces
"""

import cv2
import os
from time import sleep
import pyttsx3

#Where to store photos
DATA_FOLDER = "PieceImages"

# All piece labels (and "None")
PIECES = [
    color+"-"+piece for color in "BW" for piece in ["King", "Queen", "Rook", "Bishop", "Knight", "Pawn"]
]
PIECES.append("None")

# Positions of the pieces.
POS = [
    letter+str(number) for letter in ['C', 'D', 'E', 'F', 'G'] for number in [2, 3, 4, 5]
]

# Number of photos to take in each position
PICS_PER_POS = 3


def main():
    # Init Video
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("PiecePics")

    # Init Voice
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)

    # Setup the data folder
    if not os.path.isdir(DATA_FOLDER):
        os.mkdir(DATA_FOLDER)

    # Do all piece types
    for piece in PIECES:
        # Voice cue of the piece to use
        engine.say(piece)
        engine.runAndWait()

        # Iterate over all positions
        for pos in POS:
            # Verbal Cue
            engine.say(pos)
            engine.runAndWait()

            for pic_count in range(PICS_PER_POS):
                # Print cue
                print(piece, pos, pic_count)

                # Wait for spacebar or escape
                k = cv2.waitKey()
                ret, frame = cam.read()
                if not ret:
                    print("failed to grab frame")
                    break
                cv2.imshow("PiecePics", frame)

                if k % 256 == 27:
                    # ESC pressed exit program
                    print("Escape hit, closing...")
                    break
                elif k % 256 == 32:
                    # SPACE pressed take photo and store image
                    path = os.path.join(DATA_FOLDER, piece)
                    if not os.path.isdir(path):
                        os.mkdir(path)

                pic_path = os.path.join(path, pos + str(pic_count) + "_day2.jpg")

                cv2.imwrite(pic_path, frame)

    # Cleanup
    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
