"""
Assists taking photos of chess games.
Iterates over chess pngs - verbally prompts the move to make and you press spacebar to take photo
Photo is labelled with the FEN and saved
"""
import cv2
import os
import chess
import chess.pgn
from time import sleep
import pyttsx3

PGN_FOLDER = "ChessPGNs"
DATA_FOLDER = "BoardData"


class MovesGenerator:
    """
    Generators Moves from PGN File
    Returns tuple containing (new_move, flag)
    where flag is 0 normally.  1 if this is the first move of a new game
    """

    def __init__(self, pgn_folder) -> None:
        self.pgn_folder = pgn_folder
        self.game_files = os.listdir(pgn_folder)
    def __iter__(self):
        self.games_iterator = self.game_files.__iter__()
        return self

    def __next__(self):

        # First try to return the next move of the current game
        try:
            return (self.cur_game_iterator.__next__(), 0)
        except:
            # Try to get the next game
            try:
                print("Getting new Game")
                self.game_path = os.path.join(self.pgn_folder, self.games_iterator.__next__())
                self.cur_game_iterator = (chess.pgn.read_game(open(self.game_path))).mainline_moves().__iter__()
                return (self.cur_game_iterator.__next__(), 1)
            except StopIteration:
                raise StopIteration


def main():
    # Init Video
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("ChessPics")
    img_counter = 0

    # Init Voice
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)

    engine.say("Hello World")

    # Init move generator
    mg = MovesGenerator(PGN_FOLDER)
    # The board
    board = chess.Board()

    # Setup the data folder
    if not os.path.isdir(DATA_FOLDER):
        os.mkdir(DATA_FOLDER)

    # Going through moves, baby
    for move in mg:
        # Input move on digital board
        if move[1]:
            board.reset()
            engine.say("New Game")
        board.push(move[0])
        print(board)
        print(move)
        engine.say(move[0])
        engine.runAndWait()

        k = cv2.waitKey()
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("ChessPics", frame)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            path = os.path.join(DATA_FOLDER, str(img_counter))
            if not os.path.isdir(path):
                os.mkdir(path)

            pic_path = os.path.join(path, "pic.jpg")
            fen_path = os.path.join(path, "fen")
            with open(fen_path, 'w+') as fen_file:
                fen_file.write(board.fen())
            cv2.imwrite(pic_path, frame)
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
