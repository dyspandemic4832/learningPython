# game.py
from draw import * # same namespace
# import draw # "new" namespace

def play_game():
    print("play_game called")

def main():
    result = play_game
    draw_game(result)

if __name__ == '__main__':
    main()