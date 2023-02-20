# Splits a File containing many pgns into individual files
from sys import argv
from os.path import join
from os import mkdir, path
import re

# All new games are marked by a line that begins with this string
NEWGAME_MARKER = "[Event "
WHITE_PLAYER_REGEX = '\[White \"[\w\/ ,.-]+\"\]'
BLACK_PLAYER_REGEX = '\[Black \"[\w\/ ,.-]+\"\]'

def main():

    if len(argv) != 3:
        print("Unexpected Usage: pgn_splitter.py <pgn_file> <output_folder> ")
        exit()

    try:
        pgns = [(NEWGAME_MARKER if i != 0 else "") + rest for i, rest in enumerate(open(argv[1]).read().split(NEWGAME_MARKER))] 
    except (OSError):
        print("File Cannot be opened")
        exit(1)

    output_path = argv[2]
    
    if not path.isdir(output_path):
        mkdir(output_path)

    wp = re.compile(WHITE_PLAYER_REGEX)
    bp = re.compile(BLACK_PLAYER_REGEX)

    for pgn in pgns[1:]:
        white_player = wp.search(pgn).group()[8:-2]
        black_player = bp.search(pgn).group()[8:-2]
        filename = (white_player + "v" + black_player).replace("/", "")
        file_path = join(output_path, filename)
        with open(file_path, "w+") as output:
            output.write(pgn)




if __name__ == "__main__":
    main()